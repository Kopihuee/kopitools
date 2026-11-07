from kopitools.args.exceptions import RegistryError, ArgError
from typing import Any

class Args:
    """
    This is the class the user get the args from.
    It contains only the args the registry was asked to save
    """

    def __init__(self, args: dict[str, Any]):
        self._args = args

        for name, value in self._args.items():
            setattr(self, name, value)

    def get(self, item: str) -> None | Any:
        return self._args.get(item, None)

    def get_all(self) -> dict[str, Any]:
        return self._args.copy()

    def __getitem__(self, item: Any) -> None | Any:
        return self._args.get(item, None)

class Registry:
    """
    This is the main class

    - Obtains the system args
    - Generates Option(s)

    Each registry allows using an entry point
    Entry points are like threads.

    Each thread has its own unique args, accessible only if the entry point is present.
    """

    def __init__(self, argv: list[str], entry_point: None | str = None):
        self.options: dict[str, Any] = {}
        self.argv = argv.copy()
        self.entry_point_found = True

        if entry_point is not None:
            if entry_point not in self.argv:
                self.entry_point_found = False

    def option(
        self,
        name: str,
        receives: Any,
        default: Any,
        attribute: str,
    ):
        try:
            key = self.argv.index(name)
        except ValueError:
            self.options.update({attribute: default})
            return

        # if argument exists (evaluated above)
        # and receives None
        # then, argument's presence means a bool
        if receives is None:
            self.options.update({attribute: not default})
            return

        try:
            value = receives(self.argv[key + 1]) # get the argument just after the key (value)
        except IndexError:
            raise ArgError(f"Missing value for: {name}")
        except ValueError:
            raise ArgError(f"Could not convert: {self.argv[key + 1]} to: {receives}")

        # erase the key and its value from args
        del self.argv[key:key + 2]

        self.options.update({attribute: value})

    def collect(self) -> Args | None:
        if not self.entry_point_found:
            return None

        return Args(self.options.copy())

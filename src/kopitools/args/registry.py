from kopitools.args.option import Option
from kopitools.args.exceptions import EntryPointNotFoundError

from typing import Any

class Args:
    def __init__(self, args: dict[str, Any]):
        self._args = args

    def __getitem__(self, key: str) -> Any:
        return self._args.get(key, None)

class Registry:
    def __init__(self, argv: list[str], entry_point: None | str = None):
        self.options: list[Option] = []
        self.argv = argv

        if entry_point is not None:
            if entry_point not in self.argv:
                message = f"Entry point: [{entry_point}] not in \"args\"!"
                raise EntryPointNotFoundError(message)

    def option(
        self,
        name: str,
        receives: Any,
        default: Any,
        attribute: str,
    ):
        self.options.append(Option(name, receives, default, attribute))

    def collect(self) -> Args:
        remaining = self.argv.copy()
        args = {}

        for opt in self.options:
            value = opt.get(remaining)
            args[opt.attribute] = value

        return Args(args)

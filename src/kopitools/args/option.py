from kopitools.args.exceptions import ArgError
from typing import Any

class Option:
    def __init__(
        self,
        name: str,
        receives: Any,
        default: Any,
        attribute: str,
    ):
        self.name = name
        self.receives = receives
        self.default = default
        self.attribute = attribute

    def get(self, remaining: list[str]) -> Any:
        try:
            key = remaining.index(self.name)
        except ValueError:
            return self.default

        if self.receives is None:
            return not self.default

        try:
            value = remaining[key + 1]
        except IndexError:
            raise ValueError(f"Missing value for: {self.name}")

        del remaining[key:key + 2]

        try:
            return self.receives(value)
        except ValueError:
            message = f"[{self.name}] could not convert \"{value}\" to {self.receives}"
            raise ArgError(message)

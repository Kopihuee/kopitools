from typing import Any

class Paint:
    def __init__(
        self,
        parsed_string: str,
        end: str,
        flush: bool,
    ):
        self.parsed_string = parsed_string
        self.end = end
        self.codes = []
        self.flush = flush

        self.BLACK     = "\033[30m"
        self.RED       = "\033[31m"
        self.GREEN     = "\033[32m"
        self.YELLOW    = "\033[33m"
        self.BLUE      = "\033[34m"
        self.MAGENTA   = "\033[35m"
        self.CYAN      = "\033[36m"
        self.WHITE     = "\033[37m"

        self.BOLD      = "\033[1m"
        self.ITALIC    = "\033[3m"
        self.UNDERLINE = "\033[4m"

        self.RESET     = "\033[0m"

    def show(self):
        print(self, end=self.end, flush=True)

    def black(self):
        self.codes.append(self.BLACK)
        return self

    def red(self):
        self.codes.append(self.RED)
        return self

    def green(self):
        self.codes.append(self.GREEN)
        return self

    def yellow(self):
        self.codes.append(self.YELLOW)
        return self

    def blue(self):
        self.codes.append(self.BLUE)
        return self

    def magenta(self):
        self.codes.append(self.MAGENTA)
        return self

    def cyan(self):
        self.codes.append(self.CYAN)
        return self

    def white(self):
        self.codes.append(self.WHITE)
        return self

    def bold(self):
        self.codes.append(self.BOLD)
        return self

    def underline(self):
        self.codes.append(self.UNDERLINE)
        return self

    def italic(self):
        self.codes.append(self.ITALIC)
        return self

    def __str__(self) -> str:
        self.codes.extend([self.parsed_string, self.RESET])
        return "".join(self.codes)

def paint(
    *args: Any,
    sep: str = " ",
    end: str = "\n",
    flush: bool = False,
) -> Paint:
    parsed_string = sep.join([str(arg) for arg in args])
    return Paint(parsed_string, end, flush)

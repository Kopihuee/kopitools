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
        self.GRAY      = "\033[90m"

        self.ORANGE    = "\033[38;5;208m"
        self.PINK      = "\033[38;5;213m"
        self.PURPLE    = "\033[38;5;129m"
        self.LIME      = "\033[38;5;118m"
        self.GOLD      = "\033[38;5;220m"
        self.BROWN     = "\033[38;5;130m"
        self.TEAL      = "\033[38;5;37m"

        self.BRIGHT_BLACK   = "\033[90m"
        self.BRIGHT_RED     = "\033[91m"
        self.BRIGHT_GREEN   = "\033[92m"
        self.BRIGHT_YELLOW  = "\033[93m"
        self.BRIGHT_BLUE    = "\033[94m"
        self.BRIGHT_MAGENTA = "\033[95m"
        self.BRIGHT_CYAN    = "\033[96m"
        self.BRIGHT_WHITE   = "\033[97m"

        self.BOLD      = "\033[1m"
        self.DIM       = "\033[2m"
        self.ITALIC    = "\033[3m"
        self.UNDERLINE = "\033[4m"
        self.BLINK     = "\033[5m"
        self.REVERSE   = "\033[7m"
        self.HIDDEN    = "\033[8m"
        self.STRIKE    = "\033[9m"

        self.BG_BLACK   = "\033[40m"
        self.BG_RED     = "\033[41m"
        self.BG_GREEN   = "\033[42m"
        self.BG_YELLOW  = "\033[43m"
        self.BG_BLUE    = "\033[44m"
        self.BG_MAGENTA = "\033[45m"
        self.BG_CYAN    = "\033[46m"
        self.BG_WHITE   = "\033[47m"
        self.BG_GRAY    = "\033[100m"

        self.BG_BRIGHT_BLACK   = "\033[100m"
        self.BG_BRIGHT_RED     = "\033[101m"
        self.BG_BRIGHT_GREEN   = "\033[102m"
        self.BG_BRIGHT_YELLOW  = "\033[103m"
        self.BG_BRIGHT_BLUE    = "\033[104m"
        self.BG_BRIGHT_MAGENTA = "\033[105m"
        self.BG_BRIGHT_CYAN    = "\033[106m"
        self.BG_BRIGHT_WHITE   = "\033[107m"

        self.RESET = "\033[0m"

    def show(self):
        print(self, end=self.end, flush=self.flush)

    def black(self):   return self._add(self.BLACK)
    def red(self):     return self._add(self.RED)
    def green(self):   return self._add(self.GREEN)
    def yellow(self):  return self._add(self.YELLOW)
    def blue(self):    return self._add(self.BLUE)
    def magenta(self): return self._add(self.MAGENTA)
    def cyan(self):    return self._add(self.CYAN)
    def white(self):   return self._add(self.WHITE)
    def gray(self):    return self._add(self.GRAY)

    def orange(self): return self._add(self.ORANGE)
    def pink(self):   return self._add(self.PINK)
    def purple(self): return self._add(self.PURPLE)
    def lime(self):   return self._add(self.LIME)
    def gold(self):   return self._add(self.GOLD)
    def brown(self):  return self._add(self.BROWN)
    def teal(self):   return self._add(self.TEAL)

    def bright_black(self):   return self._add(self.BRIGHT_BLACK)
    def bright_red(self):     return self._add(self.BRIGHT_RED)
    def bright_green(self):   return self._add(self.BRIGHT_GREEN)
    def bright_yellow(self):  return self._add(self.BRIGHT_YELLOW)
    def bright_blue(self):    return self._add(self.BRIGHT_BLUE)
    def bright_magenta(self): return self._add(self.BRIGHT_MAGENTA)
    def bright_cyan(self):    return self._add(self.BRIGHT_CYAN)
    def bright_white(self):   return self._add(self.BRIGHT_WHITE)

    def bold(self):      return self._add(self.BOLD)
    def dim(self):       return self._add(self.DIM)
    def italic(self):    return self._add(self.ITALIC)
    def underline(self): return self._add(self.UNDERLINE)
    def blink(self):     return self._add(self.BLINK)
    def reverse(self):   return self._add(self.REVERSE)
    def hidden(self):    return self._add(self.HIDDEN)
    def strike(self):    return self._add(self.STRIKE)

    def bg_black(self):   return self._add(self.BG_BLACK)
    def bg_red(self):     return self._add(self.BG_RED)
    def bg_green(self):   return self._add(self.BG_GREEN)
    def bg_yellow(self):  return self._add(self.BG_YELLOW)
    def bg_blue(self):    return self._add(self.BG_BLUE)
    def bg_magenta(self): return self._add(self.BG_MAGENTA)
    def bg_cyan(self):    return self._add(self.BG_CYAN)
    def bg_white(self):   return self._add(self.BG_WHITE)
    def bg_gray(self):    return self._add(self.BG_GRAY)

    def bg_bright_black(self):   return self._add(self.BG_BRIGHT_BLACK)
    def bg_bright_red(self):     return self._add(self.BG_BRIGHT_RED)
    def bg_bright_green(self):   return self._add(self.BG_BRIGHT_GREEN)
    def bg_bright_yellow(self):  return self._add(self.BG_BRIGHT_YELLOW)
    def bg_bright_blue(self):    return self._add(self.BG_BRIGHT_BLUE)
    def bg_bright_magenta(self): return self._add(self.BG_BRIGHT_MAGENTA)
    def bg_bright_cyan(self):    return self._add(self.BG_BRIGHT_CYAN)
    def bg_bright_white(self):   return self._add(self.BG_BRIGHT_WHITE)

    def reset(self):
        return self._add(self.RESET)

    def _add(self, code: str):
        self.codes.append(code)
        return self

    def __str__(self) -> str:
        return "".join([*self.codes, self.parsed_string, self.RESET])


def paint(
    *args: Any,
    sep: str = " ",
    end: str = "\n",
    flush: bool = False,
) -> Paint:
    parsed_string = sep.join(str(arg) for arg in args)
    return Paint(parsed_string, end, flush)

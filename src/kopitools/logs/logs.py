from kopitools.paint import paint

from typing import Any

class Log:
    icons = True
    text = False

    def __init__(self, args: tuple[Any]):
        self.args = args

    def success(self):
        icon = "SUCCESS" if Log.text else "&"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().green(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

    def error(self):
        icon = "ERROR" if Log.text else "X"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().red(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

    def warning(self):
        icon = "WARNING" if Log.text else "!"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().yellow(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

    def critical(self):
        icon = "CRITICAL" if Log.text else "#"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().red(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

    def unknown(self):
        icon = "UNKNOWN" if Log.text else "?"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().magenta(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

    def info(self):
        icon = "INFO" if Log.text else "^"

        flag = paint(
            paint("[").bold(),
            paint(icon).bold().blue(),
            paint("]").bold(),
            sep=""
        )

        paint(
            paint(flag).bold(),
            paint(*self.args)
        ).show()

def log(*args: Any) -> Log:
    return Log(args)

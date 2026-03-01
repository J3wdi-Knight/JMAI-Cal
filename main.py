from sys import argv, exit

import uvicorn
from gcal import CalendarApp


def main():
    if len(argv) == 1:
        tui = CalendarApp()
        tui.run()
        return
    if len(argv) == 2 and argv[1].lower() == "api":
        uvicorn.run("app:app", host="localhost", port=8000, reload=False)
    else:
        print("Wrong argument")
        exit(1)


if __name__ == "__main__":
    main()

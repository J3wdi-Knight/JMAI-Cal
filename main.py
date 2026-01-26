import time

from cal import Calendar

# from gcal import StopwatchApp
from timer import ShabbasTimer


def main():
    cal = Calendar()
    # app = StopwatchApp()
    # app.run()
    timer = ShabbasTimer()
    # print(cal.get_current_month)
    while True:
        # time_until = timer.get_time_until()
        # print(time_until)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

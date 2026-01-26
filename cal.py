import calendar
from datetime import datetime

from textual.widgets import Static


class Calendar(Static):
    def __init__(self):
        super().__init__()
        self.date = datetime.now()

    @property
    def get_current_month(self):
        return calendar.month(self.date.year, self.date.month)

    def render(self):
        return calendar.month(self.date.year, self.date.month)

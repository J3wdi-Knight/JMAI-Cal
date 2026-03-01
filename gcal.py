from stimer import ShabbasTimer
from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Label


class CalendarApp(App):
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label("Shabbat start in ...", id="output")
        yield Button("Wanna know", id="yes")
        yield Button("Exit", id="exit")
        yield Footer()

    def on_mount(self) -> None:
        self.screen.styles.border = ("round", "white")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            timer = ShabbasTimer()
            self.query_one("#output", Label).update(timer.get_time())
        if event.button.id == "exit":
            self.exit()

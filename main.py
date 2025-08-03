from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Center
from textual.widgets import Label, Button, Header, Static, Placeholder
from tkinter import filedialog

class FiletypeConverter(Screen):
    pass

class Scaler(Screen):
    pass

class ConvertingFiletypeLoading(Screen):
    pass

class ScalingLoading(Screen):
    pass

class RemovingBackgroundLoading(Screen):
    pass

class ImageTerminalApp(App):

    CSS_PATH = "style.tcss"

    def on_mount(self) -> None:
        self.screen.styles.background = "red"

    def compose(self) -> ComposeResult:
                yield Header(show_clock=True)
                with Center():
                    yield Label("Image Terminal: An Image Manipulation Program", id="title")
                with Center():
                    yield Button("Upload Image!", id="upload_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.wepg *.avif")]
        global file_path
        file_path = filedialog.askopenfilename()
        self.exit(event.button.id)

if __name__ == "__main__":
    app = ImageTerminalApp()
    app.run()
    print(file_path)
    from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Center
from textual.widgets import Label, Button, Header, Static, Placeholder
from tkinter import filedialog

class FiletypeConverter(Screen):
    pass

class Scaler(Screen):
    pass

class ConvertingFiletypeLoading(Screen):
    pass

class ScalingLoading(Screen):
    pass

class RemovingBackgroundLoading(Screen):
    pass

class ImageTerminalApp(App):

    CSS_PATH = "style.tcss"

    def on_mount(self) -> None:
        self.screen.styles.background = "red"

    def compose(self) -> ComposeResult:
                yield Header(show_clock=True)
                with Center():
                    yield Label("Image Terminal: An Image Manipulation Program", id="title")
                with Center():
                    yield Button("Upload Image!", id="upload_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.wepg *.avif")]
        global file_path
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        self.exit(event.button.id)

if __name__ == "__main__":
    app = ImageTerminalApp()
    app.run()
    try:
        print(file_path)
    except NameError:
        print("No file was selected.")
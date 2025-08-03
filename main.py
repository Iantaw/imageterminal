from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Center, Horizontal, Vertical
from textual.widgets import Label, Button, Header, Footer
from textual.widget import Widget
from tkinter import filedialog
from PIL import Image
import pillow_avif
import tkinter as tk

global img
img = None

class ToolSelector(Screen):
    CSS_PATH = "style.tcss"
    BINDINGS = [("escape", "app.pop_screen", "To Previous Page")]

    def on_mount(self) -> None:
        self.screen.styles.background = "red"

    def compose(self) -> ComposeResult:
            yield Header(show_clock=True)
            yield Footer()
            with Center():
                yield Button("Change Filetype", id="selectBt1")
            with Center():
                yield Button("Remove Background", id="selectBt2")
            with Center():
                yield Button("Scale Image", id="selectBt3")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "selectBt1":
            self.app.push_screen(FiletypeConverter())
        elif event.button.id == "selectBt2":
            self.app.push_screen(RemovingBackground())
        elif event.button.id == "selectBt3":
            self.app.push_screen(Scaler())
        else:
            pass
    
class FiletypeConverter(Screen):
    CSS_PATH = "style.tcss"
    BINDINGS = [("escape", "app.pop_screen", "To Previous Page")]

    def on_mount(self) -> None:
        self.screen.styles.background = "red"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

        with Vertical(id="main-container"):
            yield Label("Select the filetype you would like to convert to:", id="conversionTitle")
            with Horizontal(id="button-container"):
                if img.format == "PNG":
                    yield Button("PNG", id="PNG", disabled=True)
                else:
                    yield Button("PNG", id="PNG")

                if img.format == "JPG":
                    yield Button("JPG", id="JPG", disabled=True)
                else:
                    yield Button("JPG", id="JPG")

                if img.format == "JPEG":
                    yield Button("JPEG", id="JPEG", disabled=True)
                else:
                    yield Button("JPEG", id="JPEG")

                if img.format == "BMP":
                    yield Button("BMP", id="BMP", disabled=True)
                else:
                    yield Button("BMP", id="BMP")

                if img.format == "WEBP":
                    yield Button("WEBP", id="WEBP", disabled=True)
                else:
                    yield Button("WEBP", id="WEBP")

                if img.format == "AVIF":
                    yield Button("AVIF", id="AVIF", disabled=True)
                else:
                    yield Button("AVIF", id="AVIF")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        filetype_map = {
        "AVIF": [("AVIF files", "*.avif")],
        "PNG": [("PNG files", "*.png")],
        "WEBP": [("WEBP files", "*.webp")],
        "BMP": [("BMP files", "*.bmp")],
        "JPEG": [("JPEG files", "*.jpeg")],
        "JPG": [("JPG files", "*.jpg")]
        }

        format_map = {
        "AVIF": "AVIF",
        "PNG": "PNG",
        "WEBP": "WEBP",
        "BMP": "BMP",
        "JPEG": "JPEG",
        "JPG": "JPEG"
        }

        file_format = format_map.get(event.button.id, None)

        filetypes = filetype_map.get(event.button.id, [("All files", "*.*")])
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        save_path = filedialog.asksaveasfilename(parent=root, filetypes=filetypes, defaultextension=filetypes[0][1][1:])
        root.destroy()
        if save_path:
            if file_format:
                img.save(save_path, format=file_format)
                app.pop_screen()
            else:
                img.save(save_path)
        else:
            pass

class Scaler(Screen):
    pass

class RemovingBackground(Screen):
    pass

class ScalingLoading(Screen):
    pass

class RemovingBackgroundLoading(Screen):
    pass

class ImageTerminalApp(App):

    CSS_PATH = "style.tcss"
    SCREENS = {"toolselect": ToolSelector}

    def on_mount(self) -> None:
        self.screen.styles.background = "red"

    def compose(self) -> ComposeResult:
                yield Header(show_clock=True)
                yield Footer()
                with Center():
                    yield Label("Image Terminal: An Image Manipulation Program", id="title")
                with Center():
                    yield Button("Upload Image!", id="upload_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "upload_button":
            filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.WEBP *.avif")]
            global file_path
            global img
            img = None
            root = tk.Tk()
            root.attributes('-topmost', True)
            root.withdraw()
            file_path = filedialog.askopenfilename(parent=root, filetypes=filetypes)
            root.destroy()
            if not file_path:
                pass
            else:
                img = Image.open(file_path)
                self.push_screen(ToolSelector())
        else:
            pass

if __name__ == "__main__":
    app = ImageTerminalApp()
    app.run()
    try:
        print(file_path)
    except NameError:
        print("No file was selected.")
    try:
        print(img.format)
    except NameError:
        print("No filetype was selected.")
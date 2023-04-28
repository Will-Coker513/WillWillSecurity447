import os
from guizero import PushButton, App, Text

app = App(title="Better than Hak5 Wifi Pineapple", bg="lightblue")

def run_external_app():
    os.system("ls")

def build_gui() -> None:
    # add a title to the GUI
    Text(app, "Better than a Hak5 Wifi Pineapple", 20, align="top", font="Marker Felt", height=5)
    # add buttons to the GUI
    PushButton(app, text="Command 1", command=run_external_app)
    PushButton(app, text="Command 2", command=run_external_app)
    PushButton(app, text="Command 3", command=run_external_app)
    PushButton(app, text="Exit", command=app.exit_full_screen)
    # add a footer to the GUI
    Text(app, "Product of Will & Will Security", 15, align="bottom", font="Marker Felt")


build_gui()
app.set_full_screen()
app.display()
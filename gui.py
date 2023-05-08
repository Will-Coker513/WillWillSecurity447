import os
from guizero import PushButton, App, Text, Window
from datetime import datetime


app = App(title="Better than Hak5 Wifi Pineapple", bg="lightblue")
def run_external_app():
    os.system("ls")

def run_nmap():
    os.system("nmap 192.168.1.1")

def run_wireshark():
    os.system("wireshark")

# build nmap window
def nmap_utility():
    window = Window(app, title="Nmap Utility", bg="lightblue", height=100)
    Text(window, "Nmap Utility", 20, align="top", font="Roboto", height=5)
    PushButton(window, text="Nmap Utility", command=run_nmap)
    Text(window, "Product of Will & Will Security", 15, align="bottom", font="Roboto")

# build wireshark window
def wireshark_utility():
    window = Window(app, title="Wireshark Utility", bg="lightblue")
    Text(window, "Wireshark Utility", 20, align="top", font="Marker Felt", height=5)
    PushButton(window, text="Start", command=run_wireshark)
    Text(window, "Product of Will & Will Security", 15, align="bottom", font="Roboto")
    

# build main menu
def build_gui() -> None:
    # add a title to the GUI
    Text(app, "Covert Clipboard", 20, align="top", font="Roboto", height=5)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    Text(app, f"{current_time}", 20, align="top")
    # add buttons to the GUI
    b1 = PushButton(app, text="Nmap Utility", command=nmap_utility)
    b2 = PushButton(app, text="Wireshark Utility", command=run_wireshark)
    b3 = PushButton(app, text="Exit Full Screen", command=app.exit_full_screen)
    b4 = PushButton(app, text="Exit", command=exit)
    # add a footer to the GUI
    # adjust button colors (not sure if theres a better way to do this)
    b1.bg = "white"
    b2.bg = "white"
    b3.bg = "white"
    b4.bg = "white"
    Text(app, "Product of Will & Will Security", 15, align="bottom", font="Marker Felt")

# start the app build
def start_gui():
    build_gui()
    app.set_full_screen()
    app.display()

# exit the app
def exit():
    app.destroy()

start_gui()
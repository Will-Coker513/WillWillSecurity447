import os
from guizero import PushButton, App, Text, Window

app = App(title="Better than Hak5 Wifi Pineapple", bg="lightblue")
def run_external_app():
    os.system("ls")

def run_nmap():
    pass
    # os.system("nmap 192.168.1.1")

def run_wireshark():
    os.system("wireshark")

# build nmap window
def nmap_utiltiy():
    window = Window(app, title="Nmap Utility", bg="lightblue", height=100)
    Text(window, "Nmap Utility", 20, align="top", font="Marker Felt", height=5)
    PushButton(window, text="Nmap Utility", command=run_nmap)
    Text(window, "Product of Will & Will Security", 15, align="bottom", font="Marker Felt")

# build wireshark window
def wireshark_utility():
    window = Window(app, title="Wireshark Utility", bg="lightblue")
    Text(window, "Wireshark Utility", 20, align="top", font="Marker Felt", height=5)
    PushButton(window, text="Start", command=run_wireshark)
    Text(window, "Product of Will & Will Security", 15, align="bottom", font="Marker Felt")
    

# build main menu
def build_gui() -> None:
    # add a title to the GUI
    Text(app, "Better than a Hak5 Wifi Pineapple", 20, align="top", font="Marker Felt", height=5)
    # add buttons to the GUI
    PushButton(app, text="Nmap Utility", command=nmap_utiltiy)
    PushButton(app, text="Wireshark Utility", command=wireshark_utility)
    PushButton(app, text="Command 3", command=run_external_app)
    PushButton(app, text="Exit Full Screen", command=app.exit_full_screen)
    PushButton(app, text="Exit", command=exit)
    # add a footer to the GUI
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
import tkinter as tk
from capture import CaptureScreen
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=512, height=512)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_recording_btn = tk.Button(self)
        self.start_recording_btn["text"] = "Start"
        self.start_recording_btn["command"] = self.start_recording
        self.start_recording_btn.pack(side="top")

        self.stop_recording_btn = tk.Button(self)
        self.stop_recording_btn["text"] = "Stop"
        self.stop_recording_btn["command"] = self.stop_recording
        self.stop_recording_btn.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def start_recording(self):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        outputfile = "_".join(timestamp.split()) + ".mkv"
        self.recorder = CaptureScreen(outputfile=outputfile)
        self.recorder.start()

    def stop_recording(self):
        self.recorder.stop()
        

def hello():
    print("Hello")


root = tk.Tk()
menubar = tk.Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

app = Application(master=root)
app.mainloop()
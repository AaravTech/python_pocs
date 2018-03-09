import tkinter as tk
from capture import CaptureScreen
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=512, height=512)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.start_recording_btn = tk.Button(self,
                                            text="Start",
                                            bg="green",
                                            fg="white",
                                            command=self.start_recording)
        self.start_recording_btn.grid()

        self.pause_recording_btn = tk.Button(self,
                                            text="Pause",
                                            bg="orange",
                                            fg="white",
                                            command=self.pause_recording)
        self.pause_recording_btn.grid()

        self.resume_recording_btn = tk.Button(self,
                                            text="Resume",
                                            bg="blue",
                                            fg="white",
                                            command=self.resume_recording)
        self.resume_recording_btn.grid()

        self.stop_recording_btn = tk.Button(self,
                                            text="Stop",
                                            bg="red",
                                            fg="white",
                                            command=self.stop_recording)

        self.stop_recording_btn.grid()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid()

    def start_recording(self):
        # self.start_recording_btn[]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        outputfile = "_".join(timestamp.split()) + ".mkv"
        self.recorder = CaptureScreen(outputfile=outputfile)
        self.recorder.start()

    def resume_recording(self):
        self.recorder.resume()

    def pause_recording(self):
        self.recorder.pause()

    def stop_recording(self):
        self.recorder.stop()


def generate_menu(root):
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)


root = tk.Tk()
root.minsize(500, 500)
generate_menu(root)

app = Application(master=root)
app.master.title("AT Recorder")
app.mainloop()
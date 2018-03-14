import tkinter as tk
from capture import CaptureScreen
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, isapp=True, name="at_recorder"):
        tk.Frame.__init__(self, name=name)
        self.grid()
        self.master.minsize(500, 500)
        self.master.title('AT Recorder')
        self.isapp = isapp
        self._generate_menu()
        self._create_widgets()

    def _create_widgets(self):
        self.start_recording_btn = tk.Button(self,
                                            text="Start",
                                            bg="green",
                                            fg="white",
                                            command=self.start_recording)
        self.start_recording_btn.grid()
        self.bind_all('<Control-s>', self.start_recording)

        self.pause_recording_btn = tk.Button(self,
                                            text="Pause",
                                            bg="orange",
                                            fg="white",
                                            state="disabled",
                                            command=self.pause_recording)
        self.pause_recording_btn.grid()
        self.bind_all('<Control-p>', self.pause_recording)

        self.resume_recording_btn = tk.Button(self,
                                            text="Resume",
                                            bg="blue",
                                            fg="white",
                                            state="disabled",
                                            command=self.resume_recording)
        self.resume_recording_btn.grid()
        self.bind_all('<Control-r>', self.resume_recording)

        self.stop_recording_btn = tk.Button(self,
                                            text="Stop",
                                            bg="red",
                                            fg="white",
                                            state="disabled",
                                            command=self.stop_recording)

        self.stop_recording_btn.grid()
        self.bind_all('<Control-x>', self.stop_recording)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid()

        self.bind_all('<Control-c>', self.master.destroy)

    def start_recording(self, event=None):
        self.start_recording_btn['state'] = 'disabled'
        self.stop_recording_btn['state'] = 'normal'
        self.pause_recording_btn['state'] = 'normal'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        outputfile = "_".join(timestamp.split()) + ".mkv"
        self.recorder = CaptureScreen(outputfile=outputfile)
        self.recorder.start()

    def resume_recording(self, event=None):
        self.pause_recording_btn['state'] = 'normal'
        self.resume_recording_btn['state'] = 'disabled'
        self.recorder.resume()

    def pause_recording(self, event=None):
        self.resume_recording_btn['state'] = 'normal'
        self.pause_recording_btn['state'] = 'disabled'
        self.recorder.pause()

    def stop_recording(self, event=None):
        self.start_recording_btn['state'] = 'normal'
        self.stop_recording_btn['state'] = 'disabled'
        self.pause_recording_btn['state'] = 'disabled'
        self.resume_recording_btn['state'] = 'disabled'
        self.recorder.stop()

    def key(self, event):
        print("pressed", repr(event.char))


    def _generate_menu(self):
        menubar = tk.Menu(self.master)

        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.master.config(menu=menubar)

if __name__ == '__main__':
    Application().mainloop()
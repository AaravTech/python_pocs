from tkinter import *
from tkinter import filedialog
from capture import CaptureScreen
from datetime import datetime

class Application(Frame):
    def __init__(self, isapp=True, name="at_recorder"):
        Frame.__init__(self, name=name)
        # self.master.minsize(100, 100)
        self.master.title('AT Recorder')
        self.isapp = isapp
        self._generate_menu()
        self._create_widgets()        
        self.grid()

    def _create_widgets(self):
        self.path_lbl = Label(self)
        self.path_lbl.grid(row=0, columnspan=3, column=0)
        self.browse_btn = Button(self, text="Browse", command=self.browsefunc)
        self.browse_btn.grid(row=0, column=3)

        o_r = 1
        self.start_recording_btn = Button(self,
                                            text="Start",
                                            bg="green",
                                            fg="white",
                                            command=self.start_recording)
        self.start_recording_btn.grid(row=o_r, column=0)
        self.bind_all('<Control-s>', self.start_recording)

        self.pause_recording_btn = Button(self,
                                            text="Pause",
                                            bg="orange",
                                            fg="white",
                                            state="disabled",
                                            command=self.pause_recording)
        self.pause_recording_btn.grid(row=o_r, column=1)
        self.bind_all('<Control-p>', self.pause_recording)

        self.resume_recording_btn = Button(self,
                                            text="Resume",
                                            bg="blue",
                                            fg="white",
                                            state="disabled",
                                            command=self.resume_recording)
        self.resume_recording_btn.grid(row=o_r, column=2)
        self.bind_all('<Control-r>', self.resume_recording)

        self.stop_recording_btn = Button(self,
                                            text="Stop",
                                            bg="red",
                                            fg="white",
                                            state="disabled",
                                            command=self.stop_recording)

        self.stop_recording_btn.grid(row=o_r, column=3)
        self.bind_all('<Control-x>', self.stop_recording)
        self.bind_all('<Control-c>', self.close_app)

    def start_recording(self, event=None):
        self.master.iconify()
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

    def close_app(self, event=None):
        self.master.destroy()

    def browsefunc(self, event=None):
        self.directory = filedialog.askdirectory()
        self.path_lbl.config(text=self.directory)

    def key(self, event):
        print("pressed", repr(event.char))


    def _generate_menu(self):
        menubar = Menu(self.master)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.master.config(menu=menubar)

if __name__ == '__main__':
    Application().mainloop()

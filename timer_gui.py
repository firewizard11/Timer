from tkinter import *
from tkinter import ttk

import timer


class TimerGUI:
    def __init__(self):
        self.timer = timer.Timer()
        self.root = Tk()
        self.root.after(500, self._update_time)

        self.frame = ttk.Frame(self.root)
        self.frame.grid_configure(column=3, row=3)

        self.lbl_title = ttk.Label(self.frame, text="Timer")
        self.lbl_title.grid(column=2, row=1)

        self.str_time = StringVar(self.frame)
        self._update_time()
        self.lbl_time = ttk.Label(self.frame, textvariable=self.str_time)
        self.lbl_time.grid(column=2, row=2)

        self.btn_start = ttk.Button(self.frame, text="Start", command=self.start_timer)
        self.btn_start.grid(column=1, row=3)

        self.btn_stop = ttk.Button(self.frame, text="Stop", command=self.stop_timer, default="disabled")
        self.btn_stop

        self.btn_reset = ttk.Button(self.frame, text="Reset", command=self.reset_timer)
        self.btn_reset.grid(column=3, row=3)

        self.root.mainloop()

    def start_timer(self):
        self.timer.start()

        self.btn_start.grid_forget()
        self.btn_stop.grid(column=1, row=3)

    def stop_timer(self):
        self.timer.stop()

        self.btn_stop.grid_forget()
        self.btn_start.grid(column=1, row=3)

    def reset_timer(self):
        pass

    def _update_time(self):
        self.str_time.set("{}h:{}m:{}s".format(
            self.timer.hr,
            self.timer.min,
            self.timer.sec
        ))
        self.root.after(500, self._update_time)


if __name__ == "__main__":
    gui = TimerGUI()
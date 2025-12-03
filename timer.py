import time
import threading


class Timer:

    def __init__(self):
        self.sec = 0
        self.min = 0
        self.hr = 0
        self.is_running = False
        self.timer_thread = threading.Thread(target=self._timer_loop)

    def start(self):
        self.is_running = True
        self.timer_thread.start()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.sec = 0
        self.min = 0
        self.hr = 0

    def _increment(self):
        self.sec += 1
        
        if self.sec > 59:
            self.sec = 0
            self.min += 1

        if self.min > 59:
            self.min = 0
            self.hr += 1

    def _timer_loop(self):
        while self.is_running:
            self._increment()
            time.sleep(1)

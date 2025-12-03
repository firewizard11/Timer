import time
import threading


class Timer:

    def __init__(self):
        self.sec = 0
        self.min = 0
        self.hr = 0
        self.timer_thread = None

    def start(self):
        pass
        
    def stop(self):
        pass

    def reset(self):
        self.sec = 0
        self.min = 0
        self.hr = 0

    def increment(self):
        self.sec += 1
        
        if self.sec > 59:
            self.sec = 0
            self.min += 1

        if self.min > 59:
            self.min = 0
            self.hr += 1

if __name__ == "__main__":
    timer = Timer()

    while True:
        print(f"{timer.hr}:{timer.min}:{timer.sec}", end='\r')

        timer.increment()

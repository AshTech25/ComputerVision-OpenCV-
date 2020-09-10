import datetime

class FPS:
    def __init__(self):
        self._start=None
        self.end=None
        self._numframes=0
    def start(self):
        self._start=datetime.datetime.now()
        return self
    def stop(self):
        self.end=datetime.datetime.now()
    def update(self):
        self._numframes=self._numframes+1
    def elapsed(self):
        return ((self.end - self._start).total_seconds())
    def fps(self):
        return (self._numframes/self.elapsed())

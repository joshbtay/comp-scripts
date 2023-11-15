from abc import ABC, abstractmethod
from time import time
class Widget(ABC):
    
    def __init__(self, draw, scr, x, y, width, height, color):
        self.buf = 0
        self.draw = draw
        self.scr = scr
        self.done = False
        self.rows, self.cols = scr.getmaxyx()
        self.ratio = 0.0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = time()
        self.visible = True
        self.color = color

    def get_dims(self):
        x=self.x(self.cols) if callable(self.x) else self.x
        y=self.y(self.rows) if callable(self.y) else self.y
        xx=self.width(self.cols) if callable(self.width) else self.width
        yy=self.height(self.rows) if callable(self.height) else self.height
        return x, y, xx, yy


    def set_visible(self, visible):
        if self.visible == visible:
            return
        self.visible = visible
        if visible:
            self.redraw()

    def set_color(self, color):
        if color != self.color:
            self.color = color

    def set_ratio(self, ratio):
        self.ratio = ratio
        self.update()

    def redraw(self):
        if not self.visible:
            return
        r,c = self.scr.getmaxyx()
        self.buf = 0
        self.rows = r
        self.cols = c
        self.refresh()
        self._update()

    def update(self):
        r,c = self.scr.getmaxyx()
        if not self.visible:
            return
        if (self.rows, self.cols) != (r,c):
            self.redraw()
        if self.ratio >= 1 and not self.done:
            self.buf = 0
            self.done = True
            self._finish()
        elif self.done:
            return
        else:
            self._update()
    
    @abstractmethod
    def _finish(self):
        pass

    @abstractmethod
    def _update(self):
        pass

    def refresh(self):
        pass

        


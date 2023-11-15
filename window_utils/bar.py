from abc import ABC, abstractmethod
from time import time
from .widget import Widget
class Bar(Widget):
    def __init__(self, draw, scr, x, y, width, height, color, done_string=" done. "):
        Widget.__init__(self, draw, scr, x, y, width, height, color)
        self.done_string = done_string

    @abstractmethod
    def  get_msg(self)->str:
        pass

    def _update(self):
        ratio = self.ratio
        x,y,xx,yy=self.get_dims()
        mid = (y+(y+yy-1))//2
        length = min(int(ratio*(xx)), xx-1)
        l = self.get_msg()
        for i in range(y,y+yy):
            if i == mid:
                if length > len(l):
                        self.draw.drawstring(i, x+self.buf, " " * (length-self.buf), self.color, False)
                        self.draw.drawstring(i, x, l, self.color, False, italic=self.done)
                else:
                    self.draw.drawstring(y, x + self.buf, l[self.buf:length], self.color, False)
                    self.draw.drawstring(y, x + length, l[length:], self.color, italic=self.done)
            else:
                self.draw.drawstring(i, x+self.buf, " " * (length - self.buf), self.color, False)
        if length > self.buf:
            self.buf = length

    def _finish(self):
        self._update()




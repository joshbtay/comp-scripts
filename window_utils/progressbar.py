from time import time
from .bar import Bar
class ProgressBar(Bar):

    def __init__(self, draw, scr, x, y, width, height, color, msg):
        Bar.__init__(self, draw, scr, x, y, width, height, color)
        self.msg = msg

    def get_msg(self):
        if self.done:
            return self.done_string
        i=min(3, int((time()*2-self.start*2)%4))
        return " " + self.msg + "." * i + " " * (3-i)

from time import time
from .bar import Bar
class TimeBar(Bar):

    def __init__(self, draw, scr, x, y, width, height, color, start, end):
        Bar.__init__(self, draw, scr, x, y, width, height, color)
        self.start_time = start
        self.end_time = end

    def get_msg(self):
        if self.done:
            return self.done_string
        t = self.end_time - time()
        return f"   {int(t//3600):02}:{int(t//60%60):02}:{int(t*10%600)/10}"

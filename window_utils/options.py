from .widget import Widget
from math import ceil
from time import time
class Options(Widget):
    def __init__(self, draw, scr, x, y, width, height, color, options):
        Widget.__init__(self, draw, scr, x, y, width, height, color)
        self.options = options
        self.selected = {key: 0.0 for key in options}
        self.colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        self.last_selected = ""

    def select(self, option):
        self.selected[option] = time()
        self.last_selected = option
        pass

    def _update(self):
        x,y,xx,yy = self.get_dims()
        xx-=1
        xpos = x
        between = xx
        for k,v in self.options.items():
            between -=len(k)+2
            between -=len(v)
        between /= (len(self.options)-1)
        t = time()
        for i,k in enumerate(self.options):
            isfg = t - self.selected[k] > .15
            self.draw.drawstring(y, round(xpos), f"[{k}]", self.colors[i%len(self.colors)], fg=isfg, bold=True)
            self.draw.drawstring(y, round(xpos)+3, self.options[k], self.colors[i%len(self.colors)])
            xpos += len(k)+2+len(self.options[k])+between



    def _finish(self):
        self._update()

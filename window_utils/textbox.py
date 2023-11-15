from .widget import Widget
class TextBox(Widget):
    def __init__(self, draw, scr, x, y, width, height, color, text):
        Widget.__init__(self, draw, scr, x, y, width, height, color)
        self.text = text
        self.split = text.split('\n')
        self.total_length = 0
        self.i_to_xy = {}
        self.refresh()


    def _update(self):
        x,y,xx,yy = self.get_dims()
        length = self.total_length
        while self.buf < length:
            i=self.buf
            yp,xp=self.i_to_xy[i]
            if xp==xx:
                self.draw.drawstring(y+yp, x+xp,'│', "red")
            else:
                self.draw.drawstring(y+yp, x+xp, self.split[yp][xp], self.color)
            self.buf +=1


    def refresh(self):
        x,y,xx,yy = self.get_dims()
        self.total_length = 0
        self.i_to_xy = {}
        k=0
        for i, row in enumerate(self.split):
            self.total_length += min(len(row), xx+1)
            for j in range(min(len(row), xx+1)):
                self.i_to_xy[k]=(i,j)
                k+=1

    def _finish(self):
        self._update()

    def set_text(self, text):
        self.text = text
        self.split = text.split('\n')
        self.ratio = 0
        self.refresh()






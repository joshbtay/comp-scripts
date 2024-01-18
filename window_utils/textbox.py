from .widget import Widget
class TextBox(Widget):
    def __init__(self, draw, scr, x, y, width, height, color, text):
        Widget.__init__(self, draw, scr, x, y, width, height, color)
        self.text = text.strip()
        self.split = text.split('\n')
        self.total_length = 0
        self.i_to_xy = {}
        self.ij_to_format = {}
        self.refresh()
        self.flags = {"red": "red",
                       "yello": "yellow",
                       "cyan": "cyan",
                       "green": "green",
                       "blue": "blue",
                       "magen": "magenta",
                       "white": "white",
                       "black": "black",
                       "bold": "bold",
                       "itali": "italic",
                       "under": "underline",
                       "dim": "dim",
                       }
        self.current_flags = set()


    def _update(self):
        x,y,xx,yy = self.get_dims()
        length = self.total_length
        while self.buf < length:
            i=self.buf
            yp,xp=self.i_to_xy[i]
            if (yp,xp) in self.ij_to_format:
                self.current_flags = self.ij_to_format[(yp,xp)]
            if yp >= yy:
                self.buf = length
                break
            elif yp == yy-1:
                self.draw.drawstring(y+yp, x+xp, '─', "red")
            elif xp==xx:
                self.draw.drawstring(y+yp, x+xp,'│', "red")
            else:
                self.draw.formatted_string(y+yp, x+xp, self.split[yp][xp], self.current_flags)
            if xp == min(xx, len(self.split[yp])-1):
                while xp < len(self.split[yp])+1:
                    if (yp,xp) in self.ij_to_format:
                        self.current_flags = self.ij_to_format[(yp,xp)]
                    xp +=1
            self.buf +=1


    def refresh(self):
        x,y,xx,yy = self.get_dims()
        self.total_length = 0
        self.split = self.text.split('\n')
        self.i_to_xy = {}
        self.ij_to_format = {}
        self.current_flags = set()
        flags = set()
        for i in range(len(self.split)):
            remove = []
            j = 0
            while j < len(self.split[i])-7:
                row=self.split[i]
                if row[j]=='\\' and row[j+1]=='<' and row[j+7] == '>':
                    if row[j+2:j+7] == "clear":
                        flags = set()
                        self.split[i] = row[:j]+row[j+8:]
                        self.ij_to_format[(i,j)] = flags.copy()
                        j-=1
                    elif row[j+2:j+7].rstrip('_') in self.flags:
                        flags.add(self.flags[row[j+2:j+7].rstrip('_')])
                        self.split[i] = row[:j]+row[j+8:]
                        self.ij_to_format[(i,j)] = flags.copy()
                        j-=1
                j+=1
        k=0
        for i, row in enumerate(self.split):
            if i == yy:
                break
            self.total_length += min(len(row), xx+1)
            for j in range(min(len(row), xx+1)):
                self.i_to_xy[k]=(i,j)
                k+=1

    def _finish(self):
        self._update()

    def set_text(self, text):
        x,y,xx,yy=self.get_dims()
        for i in range(yy):
            self.draw.drawstring(y+i, x, ' ' * xx, 'default')
        self.buf = 0
        self.text = text
        self.ratio = 0
        self.refresh()
        self.update()






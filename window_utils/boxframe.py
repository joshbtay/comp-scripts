from .widget import Widget
class BoxFrame(Widget):
    def __init__(self, draw, scr, x, y, width, height, color, title="",subtitle="", footer="", style=0, ):
        Widget.__init__(self, draw, scr, x, y, width, height, color)
        self.box_sides = ["╭╮╰╯─│", "╔╗╚╝═║", "╭╮╰╯╌╎"]
        self.style = style
        self.title = title
        self.subtitle = subtitle
        self.footer = footer
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
    def _update(self):
        ratio = self.ratio
        x,y,xx,yy=self.get_dims()
        total_length = xx*2+yy*2-4
        length = min(int(total_length * ratio), total_length)
        while self.buf < length:
            i=self.buf
            box_sides = self.box_sides[self.style]
            c=box_sides[-1]
            cx=x+i
            cy=y
            if i == 0:
                c=box_sides[0]
            elif i < xx-1:
                c=box_sides[4]
            elif i == xx-1:
                c=box_sides[1]
            elif i < xx+yy-2:
                c=box_sides[5]
                cx = x+xx-1
                cy += i-xx+1
            elif i == xx+yy-2:
                c=box_sides[3]
                cx = x+xx-1
                cy = y+yy-1
            elif i < 2*xx+yy-3:
                c = box_sides[4]
                cx = x+xx-(i-xx-yy+3)
                cy = y+yy-1
            elif i == 2*xx+yy-3:
                c=box_sides[2]
                cx = x
                cy = y+yy-1
            else:
                c = box_sides[5]
                cx = x
                cy += yy-(i-xx*2-yy)-4
            self.draw.drawstring(cy,cx,c,self.color)
            self.buf += 1
        j = 0
        sub = 0
        current_flags = set()
        while j < len(self.title):
            if j < len(self.title)-7 and self.title[j]=='\\' and self.title[j+1] == '<' and self.title[j+7] == '>':
                key = self.title[j+2:j+7].rstrip('_')
                if key == "clear":
                    current_flags = set()
                elif key in self.flags:
                    current_flags.add(self.flags[key])
                j+=8
                sub += 8
            else:
                self.draw.formatted_string(y, x+2+j-sub, self.title[j], current_flags if current_flags else {self.color})
                j+=1
        self.draw.drawstring(y,x+3+len(self.title)-sub,self.subtitle,self.color)
        self.draw.drawstring(y+yy-1,x+xx-2-len(self.footer),self.footer,self.color)
    def _finish(self):
        self._update()

    def set_title(self, title,is_title=True, is_subtitle=False,is_footer=False):
        if is_title:
            self.title = title
        elif is_subtitle:
            self.subtitle = title
        elif is_footer:
            self.footer = title
        self.redraw()



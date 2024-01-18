import _curses
from curses import *
from collections import defaultdict
class Draw:
    def __init__(self, scr):
        self.scr = scr
        self.colors = defaultdict(lambda: color_pair(0))
        i = 1
        self.color_ids = ["red", "yellow", "blue", "cyan", "green", "magenta", "white", "black", "default"]
        curses_colors = [COLOR_RED, COLOR_YELLOW, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN, COLOR_MAGENTA, COLOR_WHITE, COLOR_BLACK, -1]
        for id, c in zip(self.color_ids, curses_colors):
            init_pair(i, COLOR_BLACK, c)
            self.colors[(id, False)] = i
            i+=1
            init_pair(i, c, -1)
            self.colors[(id, True)] = i
            i+=1


    def drawstring(self, r, c, text, color, fg=True, italic=False, bold=False, underline=False, dim=False):
        style = color_pair(self.colors[(color, fg)])
        if italic:
            style|=A_ITALIC
        if bold:
            style|=A_BOLD
        if underline:
            style|=A_UNDERLINE
        if dim:
            style|=A_DIM

        try:
            self.scr.addstr(r,c,text,style)
        except _curses.error as e:
            pass

    def formatted_string(self, r, c, text, flags):
        color = "white"
        for flag in flags:
            if flag in self.color_ids:
                color = flag
        fg = "bg" not in flags
        bold = "bold" in flags
        italic = "italic" in flags
        underline = "underline" in flags
        dim = "dim" in flags
        self.drawstring(r, c, text, color, fg, italic, bold, underline, dim)



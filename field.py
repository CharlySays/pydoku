import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk


class Field(Gtk.Button):

    def __init__(self, value, fixed):
        Gtk.ToggleButton.__init__(self, label=value, expand=True)
        if fixed:
            self.set_name('fixed')


    def button_clicked(self, button, grid):
        x = 0
        s=''
        for f in grid:
            if x%9 == 0:
                s += '\n'

            if f.get_label() == '':
                s += '_'
            else:
                s += f.get_label()
            x += 1

        print(s)

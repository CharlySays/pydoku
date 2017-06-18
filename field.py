import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk


class Field(Gtk.Button):

    def __init__(self, value, name):
        Gtk.ToggleButton.__init__(self, label=value, expand=True)
        self.set_name(name)


    def button_clicked(self, button, grid):
       pass

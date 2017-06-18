import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from controll import *


class Field(Gtk.Button):
    def __init__(self, value, name):
        Gtk.ToggleButton.__init__(self, label=value, expand=True)
        self.set_name(name)

    def button_clicked(self, event, grid):
        set_hints(self, grid)

    def button_focused(self, widget, event, grid):
        set_hints(widget, grid)

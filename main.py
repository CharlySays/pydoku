import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from mainWindow import *
from field import *
from newGameWindow import *

style_provider = Gtk.CssProvider()

style_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

mainwindow = MainWindow()
mainwindow.set_name('MainWindow')
mainwindow.connect("delete-event", Gtk.main_quit)

Gtk.main()
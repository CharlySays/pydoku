import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from mainWindow import *
from field import *

style_provider = Gtk.CssProvider()

style_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

window = MainWindow()
window.set_name('MainWindow')
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
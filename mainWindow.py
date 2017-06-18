import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import math

from field import *

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sudoku")
        self.set_size_request(400, 400)
        self.set_border_width(5)
        layout = Gtk.Grid()
        self.add(layout)

        #Setup Menu
        mb = Gtk.MenuBar()


        drop_file_menu = Gtk.MenuItem("File")
        file_menu = Gtk.Menu()

        file_menu_save = Gtk.MenuItem("Save")
        file_menu_load = Gtk.MenuItem("Load...")
        file_menu_exit = Gtk.MenuItem("Exit")

        drop_file_menu.set_submenu(file_menu)
        file_menu.append(file_menu_load)
        file_menu.append(file_menu_save)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_menu_exit)

        drop_game_menu = Gtk.MenuItem("Game")
        game_menu = Gtk.Menu()

        game_menu_reset = Gtk.MenuItem("Reset")
        game_menu_new = Gtk.MenuItem("New Game")

        drop_game_menu.set_submenu(game_menu)
        game_menu.append(game_menu_new)
        game_menu.append(game_menu_reset)

        mb.append(drop_file_menu)
        mb.append(drop_game_menu)

        layout.attach(mb,0,0,1,1)

        # Setup a Sudoku-Style table
        table = Gtk.Table(9, 9, True)
        table.set_row_spacing(2, 7)
        table.set_row_spacing(5, 7)

        table.set_col_spacing(2, 7)
        table.set_col_spacing(5, 7)

        # Setup an empty Grid and attach it to my table
        self.grid = []
        for i in range(81):
            self.grid.append(Field('', False))
            table.attach(self.grid[i], math.floor(i / 9), math.floor(i / 9) + 1, (i % 9), (i % 9) + 1)

        layout.attach(table,0,1,1,1)

        for f in self.grid:
            f.connect("clicked", f.button_clicked, self.grid)

        self.connect('key_press_event', self.on_key_press, self.grid)

    def on_key_press(self, widget, event, grid):
        if event.keyval == 65307:
            Gtk.main_quit()

        f = widget.get_focus()
        if f in grid:
            if event.keyval == 65457 or event.keyval == 49:
                f.set_label('1')
            elif event.keyval == 65458 or event.keyval == 50:
                f.set_label('2')
            elif event.keyval == 65459 or event.keyval == 51:
                f.set_label('3')
            elif event.keyval == 65460 or event.keyval == 52:
                f.set_label('4')
            elif event.keyval == 65461 or event.keyval == 53:
                f.set_label('5')
            elif event.keyval == 65462 or event.keyval == 54:
                f.set_label('6')
            elif event.keyval == 65463 or event.keyval == 55:
                f.set_label('7')
            elif event.keyval == 65464 or event.keyval == 56:
                f.set_label('8')
            elif event.keyval == 65465 or event.keyval == 57:
                f.set_label('9')
            elif event.keyval == 65288 or event.keyval == 48 or event.keyval == 65456 or event.keyval == 65535:
                f.set_label('')
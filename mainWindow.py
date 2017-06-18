import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import math, random

from field import *
from generator import *
from controll import *
from newGameWindow import *

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sudoku")
        self.set_size_request(400, 400)
        self.set_border_width(5)
        layout = Gtk.Grid()
        self.add(layout)
        self.grid = []

        self.newgamewindow = NewGameWindow(self)
        self.newgamewindow.set_name('NewGame')
        self.newgamewindow.connect('delete-event', Gtk.main_quit)

        # Setup a Sudoku-Style table
        table = Gtk.Table(9, 9, True)
        table.set_row_spacing(2, 7)
        table.set_row_spacing(5, 7)

        table.set_col_spacing(2, 7)
        table.set_col_spacing(5, 7)

        # Setup an empty Grid
        self.initgrid()

        # Setup menu
        layout.attach(self.initmenu(), 0, 0, 1, 1)

        for i in range(9):
            for j in range(9):
                table.attach(self.grid[i][j], j, j + 1, (i % 9), (i % 9) + 1)

        layout.attach(table, 0, 1, 1, 1)

        for r in self.grid:
            for f in r:
                f.connect('focus-in-event', f.button_focused, self.grid)
                f.connect('clicked', f.button_clicked, self.grid)

        self.connect('key_press_event', on_key_press, self.grid)


        self.newgamewindow.show_all()

    def initgrid(self):
        for i in range(0, 9):
            row = []
            for j in range(0, 9):
                row.append(Field('', ''))
            self.grid.append(row)

    def initmenu(self):
        mb = Gtk.MenuBar()

        mb.append(self.init_menu_file())
        mb.append(self.init_menu_game())

        return mb

    def init_menu_game(self):
        drop_game_menu = Gtk.MenuItem("Game")
        game_menu = Gtk.Menu()

        game_menu_reset = Gtk.MenuItem("Reset")
        game_menu_new = Gtk.MenuItem("New Game")
        new_game_menu = Gtk.Menu()

        game_menu_new.set_submenu(new_game_menu)

        new_game_menu_easy = Gtk.MenuItem("Easy")
        new_game_menu_medium = Gtk.MenuItem("Medium")
        new_game_menu_hard = Gtk.MenuItem("Hard")

        new_game_menu_easy.connect('activate', new_game_clicked, self.grid, 30)
        new_game_menu_medium.connect('activate', new_game_clicked, self.grid, 40)
        new_game_menu_hard.connect('activate', new_game_clicked, self.grid, 50)
        game_menu_reset.connect('activate', reset_game, self.grid)

        new_game_menu.append(new_game_menu_easy)
        new_game_menu.append(new_game_menu_medium)
        new_game_menu.append(new_game_menu_hard)

        game_menu.append(game_menu_new)
        game_menu.append(game_menu_reset)
        drop_game_menu.set_submenu(game_menu)

        return drop_game_menu

    def init_menu_file(self):
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

        return drop_file_menu

    def check_filled(self):
        for row in self.grid:
            for field in row:
                if field.get_label() == '':
                    return False

        return True
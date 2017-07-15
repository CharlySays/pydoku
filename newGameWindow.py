import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import math, random

from field import *
from generator import *
from controll import *


class NewGameWindow(Gtk.Window):
    def __init__(self, mainwindow):
        Gtk.Window.__init__(self, title="New Game")
        self.set_size_request(200, 300)
        self.set_border_width(5)
        layout = Gtk.Grid()
        self.add(layout)

        easy = Gtk.Button('Easy', expand=True)
        medium = Gtk.Button('Medium', expand=True)
        hard = Gtk.Button('Hard', expand=True)

        easy.connect('clicked', self.new_game_clicked, mainwindow, 30)
        medium.connect('clicked', self.new_game_clicked, mainwindow, 40)
        hard.connect('clicked', self.new_game_clicked, mainwindow, 50)

        layout.attach(easy, 0, 0, 1, 1)
        layout.attach(medium, 0, 1, 1, 1)
        layout.attach(hard, 0, 2, 1, 1)

    def new_game_clicked(self, event, mainwindow, difficulty):
        generateGrid(mainwindow.grid, difficulty)
        mainwindow.show_all()
        mainwindow.s = 0
        self.hide()



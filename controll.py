import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from generator import *


def on_key_press(widget, event, grid):
    if event.keyval == 65307:
        Gtk.main_quit()

    f = widget.get_focus()
    if any(f in sub for sub in grid) and not f.get_name() == 'fixed':
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

        if widget.check_filled():
            if solvePuzzle(grid,0,0):
                widget.hide()
                widget.newgamewindow.show_all()

        set_hints(f, grid)


def new_game_clicked(event, mainwindow, difficulty):
    generateGrid(mainwindow.grid, difficulty)
    mainwindow.s = 0

def reset_game(event, mainwindow):
    for row in mainwindow.grid:
        for field in row:
            if field.get_name() not in ['fixed', 'marked_fixed']:
                field.set_label('')

    mainwindow.s = 0

def set_hints(widget, grid):
    was_fixed = False
    if widget.get_name() in ['fixed', 'marked_fixed']:
        was_fixed = True

    for row in grid:
        for field in row:
            if field.get_name() == 'marked_fixed':
                field.set_name('fixed')
            if field.get_name() == 'marked':
                field.set_name('')

    if widget.get_label() != '':
        for row in grid:
            for field in row:
                if widget.get_label() == field.get_label():
                    if field.get_name() == 'fixed':
                        field.set_name('marked_fixed')
                    if field.get_name() == '':
                        field.set_name('marked')

    if was_fixed:
        widget.set_name('fixed')
    else:
        widget.set_name('')

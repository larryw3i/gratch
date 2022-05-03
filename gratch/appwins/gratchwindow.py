import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest
from tkinter import *

import gi

from gratch.locale import _
from gratch.settings import gi_require_version
from gratch.widgets.mainwindow import MainWindow

gi.require_version(*gi_require_version)
from gi.repository import Gtk

root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


class GratchWindow:
    def __init__(
        self, appid=None, test=False, default_width=None, default_height=None
    ):
        self.appid = appid or "fun.larryw3i.gratch"
        self.app = Gtk.Application(application_id=self.appid)
        self.win = None
        self._test = test
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_width = default_width or self.get_screen_width_of(2)
        self.default_height = default_height or self.get_screen_height_of(2)

    def get_screen_width_of(self, of):
        return int(self.screen_width / of)

    def get_screen_height_of(self, of):
        return int(self.screen_height / of)

    def test(self):
        print(_("test!"))

    def set_childs(self):
        pass

    def on_activate(self, app):
        self.win = Gtk.ApplicationWindow(
            application=self.app,
            default_width=self.default_width,
            default_height=self.default_height,
        )
        self.set_childs()
        self.win.present()

    def connect(self):
        self.app.connect("activate", self.on_activate)

    def run(self):
        self.connect()
        self._test and self.test()
        self.app.run(None)

import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest

import gi

from gratch.locale import _
from gratch.widgets.mainwindow import MainWindow

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from tkinter import *

root= Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


class GratchWindow:
    def __init__(
        self, appid=None, test=True, default_width=None, default_height=None
    ):
        self.appid = appid or "fun.larryw3i.gratch"
        self.app = Gtk.Application(application_id=self.appid)
        self.win = None
        self._test = test
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.default_width = default_width or 500
        self.default_height = default_height or 200

    def test(self):
        print(_("test!"))

    def set_childs(self):
        self.btn = Gtk.Button(label=_("Hello, World!"))
        self.btn.connect("clicked", lambda x: self.win.close())
        self.win.set_child(self.btn)

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

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


class GratchWindow:
    def __init__(self, appid=None, test=True):
        self.app = Gtk.Application(
            application_id=appid or "fun.larryw3i.gratch"
        )
        self.win = None
        self._test = test

    def test(self):
        print(_("test!"))

    def set_childs(self):
        self.btn = Gtk.Button(label=_("Hello, World!"))
        self.btn.connect("clicked", lambda x: self.win.close())
        self.win.set_child(self.btn)

    def on_activate(self, app):
        self.win = Gtk.ApplicationWindow(application=self.app)
        self.set_childs()
        self.win.present()

    def connect(self):
        self.app.connect("activate", self.on_activate)

    def run(self):
        self.connect()
        if self._test:
            self.test()
        self.app.run(None)

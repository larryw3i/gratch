import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest

import gi

from gratch.appwins.gratchwindow import GratchWindow
from gratch.locale import _

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def go(test=True):
    if test:
        print(_("Hello, World!"))
    gratchwin = GratchWindow()
    gratchwin.run()

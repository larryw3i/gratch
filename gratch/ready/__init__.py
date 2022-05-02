import importlib
import os
import pickle
import subprocess
import threading
import webbrowser
from functools import partial
from itertools import zip_longest

from gratch.locale import _
from gratch.widgets.mainwindow import MainWindow


def go(test=True):
    if test:
        print(_('Hello, World!'))
    pass

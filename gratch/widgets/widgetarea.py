import importlib
import os
import pickle
import subprocess
import threading
import tkinter as tk
import webbrowser
from functools import partial
from itertools import zip_longest
from tkinter import *
from tkinter import ttk

from gratch.locale import _
from gratch.widgets.areabase import AreaBase


class WidgetArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)

    def place(self):
        self.separator.place(
            x=self.win.get_w_width(of=3), y=0, relwidth=0.2, relheight=1
        )

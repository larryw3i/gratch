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


class PresentationArea(AreaBase):
    def __init__(self, win, width=None):
        super().__init__(win, width)

    def place(self):
        pass

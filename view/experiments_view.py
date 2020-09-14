import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("view/ui/experiments_view.ui")[0]


class ExperimentsView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
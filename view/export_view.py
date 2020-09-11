import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("view/ui/export_view.ui")[0]


class ExportView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("view/ui/pre_conditioning_view.ui")[0]


class PreConditioningView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
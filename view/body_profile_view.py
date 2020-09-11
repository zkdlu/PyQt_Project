import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("view/ui/body_profile.ui")[0]


class BodyProfileView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
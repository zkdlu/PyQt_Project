import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("view/ui/clothing_property_view.ui")[0]


class ClothingPropertyView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
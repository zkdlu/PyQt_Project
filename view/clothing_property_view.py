from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/clothing_property_view.ui")[0]


class ClothingPropertyView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_file.clicked.connect(self.on_select_file)

    def on_select_file(self):
        my_util.set_table_with_txt(self, self.txt_file, self.table_clothing_property)
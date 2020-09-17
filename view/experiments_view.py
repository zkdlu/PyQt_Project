import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/experiments_view.ui")[0]


class ExperimentsView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_steady_file.clicked.connect(self.on_select_file)

    def on_select_file(self):
        my_util.set_table_with_txt(self, self.txt_steady_file, self.table_steady_experiments)
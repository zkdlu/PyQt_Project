import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/experiments_view.ui")[0]


class ExperimentsView(QMainWindow, form_class):
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __init__(self):
        super().__init__()
        self.SteadyState = {}

        self.setupUi(self)

        self.btn_ok.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

        self.btn_steady_file.clicked.connect(self.on_select_file)

    def on_select_file(self):
        my_util.set_table_with_txt(self, self.txt_steady_file, self.table_steady_experiments)
        my_util.get_dic_from_table(self.SteadyState, self.table_steady_experiments)
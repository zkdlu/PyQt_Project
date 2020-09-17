from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/pre_conditioning_view.ui")[0]


class PreConditioningView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

        self.btn_file.clicked.connect(self.on_select_file)

    def on_select_file(self):
        my_util.set_table_with_txt(self, self.txt_file, self.table_pre_conditioning)
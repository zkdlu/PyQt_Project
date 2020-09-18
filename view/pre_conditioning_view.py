from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/pre_conditioning_view.ui")[0]


class PreConditioningView(QMainWindow, form_class):
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __init__(self):
        super().__init__()
        self.PreConditioning = {}

        self.setupUi(self)

        self.btn_ok.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

        self.btn_file.clicked.connect(self.on_select_file)

    def on_select_file(self):
        my_util.set_table_with_txt(self, self.txt_file, self.table_pre_conditioning)
        my_util.get_dic_from_table(self.PreConditioning, self.table_pre_conditioning)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/tsv_csv_profile_view.ui")[0]


class TsvCsvProfileView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox_skin_set_temperature.currentTextChanged.connect(self.on_skin_set_temperature)
        self.comboBox_overall_factor.currentTextChanged.connect(self.on_overall_factor)
        self.comboBox_sensation_coefficient.currentTextChanged.connect(self.on_sensation_coefficient)
        self.comboBox_comfort_sensation.currentTextChanged.connect(self.on_comfort_sensation)

    def on_skin_set_temperature(self, value):
        my_util.set_table(self, self.comboBox_skin_set_temperature,
                          self.table_skin_set_temperature, value)

    def on_overall_factor(self, value):
        my_util.set_table(self, self.comboBox_overall_factor,
                          self.table_overall_factor, value)

    def on_sensation_coefficient(self, value):
        my_util.set_table(self, self.comboBox_sensation_coefficient,
                          self.table_sensation_coefficient, value)

    def on_comfort_sensation(self, value):
        my_util.set_table(self, self.comboBox_comfort_sensation,
                          self.table_comfort_sensation, value)
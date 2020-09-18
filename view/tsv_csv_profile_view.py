from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/tsv_csv_profile_view.ui")[0]


class TsvCsvProfileView(QMainWindow, form_class):
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __init__(self):
        super().__init__()
        self.SkinSetTemperature = {}
        self.OverallSensationWeightingFactor = {}
        self.ThermalSensationCoefficient = {}
        self.ComfortSensationCoefficient = {}

        self.setupUi(self)

        self.btn_ok.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

        self.comboBox_skin_set_temperature.currentTextChanged.connect(self.on_skin_set_temperature)
        self.comboBox_overall_factor.currentTextChanged.connect(self.on_overall_factor)
        self.comboBox_sensation_coefficient.currentTextChanged.connect(self.on_sensation_coefficient)
        self.comboBox_comfort_sensation.currentTextChanged.connect(self.on_comfort_sensation)

    def on_skin_set_temperature(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_skin_set_temperature,
                                        self.table_skin_set_temperature, value)
        my_util.get_dic_from_table(self.SkinSetTemperature, self.table_skin_set_temperature)

    def on_overall_factor(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_overall_factor,
                                        self.table_overall_factor, value)
        my_util.get_dic_from_table(self.OverallSensationWeightingFactor, self.table_overall_factor)

    def on_sensation_coefficient(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_sensation_coefficient,
                                        self.table_sensation_coefficient, value)
        my_util.get_dic_from_table(self.ThermalSensationCoefficient, self.table_sensation_coefficient)

    def on_comfort_sensation(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_comfort_sensation,
                                        self.table_comfort_sensation, value)
        my_util.get_dic_from_table(self.ComfortSensationCoefficient, self.table_comfort_sensation)
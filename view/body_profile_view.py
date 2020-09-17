import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv
from view import my_util

form_class = uic.loadUiType("view/ui/body_profile_view.ui")[0]


class BodyProfileView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox_body_area_weight.currentTextChanged.connect(self.on_body_area_weight)
        self.comboBox_heat_capacity.currentTextChanged.connect(self.on_heat_capacity)
        self.comboBox_metabolic_rate.currentTextChanged.connect(self.on_metabolic_rate)
        self.comboBox_heat_production_rate.currentTextChanged.connect(self.on_heat_production_rate)

    def on_body_area_weight(self, value):
        my_util.set_table(self, self.comboBox_body_area_weight, self.table_body_area_weight, value)

    def on_heat_capacity(self, value):
        my_util.set_table(self, self.comboBox_heat_capacity, self.table_heat_capacity, value)

    def on_metabolic_rate(self, value):
        my_util.set_table(self, self.comboBox_metabolic_rate, self.table_metabolic_rate, value)

    def on_heat_production_rate(self, value):
        my_util.set_table(self, self.comboBox_heat_production_rate, self.table_heat_production_rate, value)

    def set_table(self, q_combobox, q_table, value):
        q_combobox.setCurrentIndex(0)
        table = self.read_csv(value)

        if table:
            csv_row_count = len(table) - 1
            q_table.setRowCount(csv_row_count)

            for y, line in enumerate(table):
                for x, item in enumerate(line):
                    q_table.setItem(y, x, QTableWidgetItem(item))

    def read_csv(self, value):
        if value == 'Custom':
            file_name = QFileDialog.getOpenFileName(self, 'Open file', './')

            if file_name[0]:
                with open(file_name[0], 'r') as f:
                    rdr = csv.reader(f)
                    next(rdr)

                    table = list(rdr)
                    return table

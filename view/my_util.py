import csv
from PyQt5.QtWidgets import *


def set_table(self, q_combobox, q_table, value):
    q_combobox.setCurrentIndex(0)
    table = read_csv(self, value)
    
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

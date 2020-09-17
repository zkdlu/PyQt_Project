import csv
from PyQt5.QtWidgets import *


def set_table_with_txt(self, q_textbox, q_table):
    file_name, table = read_csv(self)

    q_textbox.setText(file_name)

    if table:
        csv_row_count = len(table) - 1
        q_table.setRowCount(csv_row_count)

        for y, line in enumerate(table):
            for x, item in enumerate(line):
                q_table.setItem(y, x, QTableWidgetItem(item))


def set_table_with_combobox(self, q_combobox, q_table, value):
    q_combobox.setCurrentIndex(0)

    if value == 'Custom':
        _, table = read_csv(self)

        if table:
            csv_row_count = len(table) - 1
            q_table.setRowCount(csv_row_count)

            for y, line in enumerate(table):
                for x, item in enumerate(line):
                    q_table.setItem(y, x, QTableWidgetItem(item))


def read_csv(self):
    file_name = QFileDialog.getOpenFileName(self, 'Open file', './', 'csv(*.csv)')

    if file_name[0]:
        with open(file_name[0], 'r') as f:
            rdr = csv.reader(f)
            next(rdr)

            table = list(rdr)
            return file_name[0], table

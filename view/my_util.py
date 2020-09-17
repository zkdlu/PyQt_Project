import csv
from PyQt5.QtWidgets import *


def get_dic_from_table(dic, q_table):
    headerCount = q_table.columnCount()
    rowCount = q_table.rowCount()

    for y in range(0, rowCount):
        cellFirst = q_table.item(y, 0).text()
        dic[cellFirst] = {}

        for x in range(1, headerCount):
            headerText = q_table.horizontalHeaderItem(x).text()
            cell = q_table.item(y, x).text()
            dic[cellFirst][headerText] = cell

    return dic


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

    if file_name != ('', ''):
        with open(file_name[0], 'r') as f:
            rdr = csv.reader(f)
            next(rdr)

            table = list(rdr)
            return file_name[0], table

    return '', ''

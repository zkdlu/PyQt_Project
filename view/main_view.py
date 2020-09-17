import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from view import *

form_class = uic.loadUiType("view/ui/main_view.ui")[0]


class MainView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.export_window = export_view.ExportView()
        self.actionExport.triggered.connect(self.export_window.show)

        self.pre_conditioning_window = pre_conditioning_view.PreConditioningView()
        self.actionPre_conditioning.triggered.connect(self.pre_conditioning_window.show)

        self.body_profile_window = body_profile_view.BodyProfileView()
        self.actionBody_profile.triggered.connect(self.body_profile_window.show)

        self.clothing_property_window = clothing_property_view.ClothingPropertyView()
        self.actionClothing_property.triggered.connect(self.clothing_property_window.show)

        self.experiments_window = experiments_view.ExperimentsView()
        self.actionExperiment.triggered.connect(self.experiments_window.show)

        self.tsv_csv_profile_window = tsv_csv_profile_view.TsvCsvProfileView()
        self.actionTSV_CSV_profile.triggered.connect(self.tsv_csv_profile_window.show)

        self.btn_test.clicked.connect(self.test)

    def test(self):
        print(self.body_profile_window['BodyAreaAndWeight']['Head'])


def show():
    app = QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    app.exec()
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from view import *

form_class = uic.loadUiType("view/ui/main_view.ui")[0]


class MainView(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.body_profile_window = body_profile_view.BodyProfileView()
        self.tsv_csv_profile_window = tsv_csv_profile_view.TsvCsvProfileView()
        self.experiments_window = experiments_view.ExperimentsView()
        self.clothing_property_window = clothing_property_view.ClothingPropertyView()
        self.pre_conditioning_window = pre_conditioning_view.PreConditioningView()
        self.export_window = export_view.ExportView()
        self.setupUi(self)

        self.actionExport.triggered.connect(self.showExport)
        self.actionPre_conditioning.triggered.connect(self.showPreConditioning)
        self.actionBody_profile.triggered.connect(self.showBodyProfile)
        self.actionClothing_property.triggered.connect(self.showClothingProperty)
        self.actionExperiment.triggered.connect(self.showExperiments)
        self.actionTSV_CSV_profile.triggered.connect(self.showTsvCsvProfile)
        self.btn_test.clicked.connect(self.test)

    def showExport(self):
        self.export_window.show()

    def showPreConditioning(self):
        self.pre_conditioning_window.show()

    def showClothingProperty(self):
        self.clothing_property_window.show()

    def showExperiments(self):
        self.experiments_window.show()

    def showTsvCsvProfile(self):
        self.tsv_csv_profile_window.show()

    def showBodyProfile(self):
        self.body_profile_window.show()

    def test(self):
        print(self.body_profile_window['BodyAreaAndWeight']['Head'])


def show():
    app = QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    app.exec()
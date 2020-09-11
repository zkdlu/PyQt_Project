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


def show():
    app = QApplication(sys.argv)
    main_window = MainView()
    main_window.show()
    app.exec()
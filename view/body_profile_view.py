from PyQt5.QtWidgets import *
from PyQt5 import uic
from view import my_util

form_class = uic.loadUiType("view/ui/body_profile_view.ui")[0]


class BodyProfileView(QMainWindow, form_class):
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __init__(self):
        super().__init__()
        self.BodyAreaAndWeight = {}
        self.HeatCapacity = {}
        self.BasalMetabolicRate = {}
        self.HeatProductionRate = {}
        self.BloodFlowRate = {}
        self.SetTemperature = {}
        self.WeightingAndDistributionCoefficient = {}
        self.ControlCoefficient = {}
        self.ConductionBetweenNode = {}
        self.NatureConvection = {}
        self.ForcedConvection = {}
        self.Radiation = {}

        self.setupUi(self)

        self.comboBox_body_area_weight.currentTextChanged.connect(self.on_body_area_weight)
        self.comboBox_heat_capacity.currentTextChanged.connect(self.on_heat_capacity)
        self.comboBox_metabolic_rate.currentTextChanged.connect(self.on_metabolic_rate)
        self.comboBox_heat_production_rate.currentTextChanged.connect(self.on_heat_production_rate)

        self.comboBox_flow_rate.currentTextChanged.connect(self.on_flow_rate)
        self.comboBox_set_temperature.currentTextChanged.connect(self.on_set_temperature)
        self.comboBox_weighting_distribution_coefficient.currentTextChanged \
            .connect(self.on_weighting_distribution_coefficient)
        self.comboBox_control_coefficient.currentTextChanged.connect(self.on_control_coefficient)

        self.comboBox_conduction.currentTextChanged.connect(self.on_conduction)
        self.comboBox_nature_convection.currentTextChanged.connect(self.on_nature_convection)
        self.comboBox_forced_convection.currentTextChanged.connect(self.on_forced_convection)
        self.comboBox_radiation.currentTextChanged.connect(self.on_radiation)

    def on_body_area_weight(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_body_area_weight,
                                        self.table_body_area_weight, value)
        my_util.get_dic_from_table(self.BodyAreaAndWeight, self.table_body_area_weight)

    def on_heat_capacity(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_heat_capacity,
                                        self.table_heat_capacity, value)
        my_util.get_dic_from_table(self.HeatCapacity, self.table_heat_capacity)

    def on_metabolic_rate(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_metabolic_rate,
                                        self.table_metabolic_rate, value)
        my_util.get_dic_from_table(self.BasalMetabolicRate, self.table_metabolic_rate)

    def on_heat_production_rate(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_heat_production_rate,
                                        self.table_heat_production_rate, value)
        my_util.get_dic_from_table(self.HeatProductionRate, self.table_heat_production_rate)

    def on_flow_rate(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_flow_rate,
                                        self.table_flow_rate, value)
        my_util.get_dic_from_table(self.BloodFlowRate, self.table_flow_rate)

    def on_set_temperature(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_set_temperature,
                                        self.table_set_temperature, value)
        my_util.get_dic_from_table(self.SetTemperature, self.table_set_temperature)

    def on_weighting_distribution_coefficient(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_weighting_distribution_coefficient,
                                        self.table_weighting_distribution_coefficient, value)
        my_util.get_dic_from_table(self.WeightingAndDistributionCoefficient,
                                   self.table_weighting_distribution_coefficient)

    def on_control_coefficient(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_control_coefficient,
                                        self.table_control_coefficient, value)
        my_util.get_dic_from_table(self.ControlCoefficient, self.table_control_coefficient)

    def on_conduction(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_conduction,
                                        self.table_conduction, value)
        my_util.get_dic_from_table(self.ConductionBetweenNode, self.table_conduction)

    def on_nature_convection(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_nature_convection,
                                        self.table_nature_convection, value)
        my_util.get_dic_from_table(self.NatureConvection, self.table_nature_convection)

    def on_forced_convection(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_forced_convection,
                                        self.table_forced_convection, value)
        my_util.get_dic_from_table(self.ForcedConvection, self.table_forced_convection)

    def on_radiation(self, value):
        my_util.set_table_with_combobox(self, self.comboBox_radiation,
                                        self.table_radiation, value)
        my_util.get_dic_from_table(self.Radiation, self.table_radiation)

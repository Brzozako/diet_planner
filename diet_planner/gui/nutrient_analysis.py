# diet_planner/gui/nutrient_analysis.py
from PyQt5.QtWidgets import QMessageBox

class NutrientAnalysis:
    def __init__(self):
        self.nutrients = {}

    def analyze_meal(self, meal):
        for nutrient, value in meal['nutrients'].items():
            if nutrient in self.nutrients:
                self.nutrients[nutrient] += value
            else:
                self.nutrients[nutrient] = value

    def report_nutrients(self):
        nutrient_report = "\n".join([f"{nutrient}: {value}" for nutrient, value in self.nutrients.items()])
        QMessageBox.information(None, "Analiza Składników Odżywczych", f"Analiza składników odżywczych:\n{nutrient_report}")

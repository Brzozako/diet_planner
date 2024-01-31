from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTabWidget

# diet_planner/utils/helpers.py

from diet_planner.gui.diet_plan_creator import DietPlanCreator, DietPlanCreatorGUI, AddMealDialog
from calorie_monitor import CalorieMonitor, CalorieMonitorGUI
from nutrient_analyzer import NutrientAnalyzer, NutrientAnalyzerGUI
from nutrition_recommendations import NutritionRecommendations, NutritionRecommendationsGUI, UserData

class DietPlannerGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Inicjalizacja modułów
        self.diet_plan_creator = DietPlanCreator()
        self.calorie_monitor = CalorieMonitor(self.diet_plan_creator)
        self.nutrient_analyzer = NutrientAnalyzer(self.diet_plan_creator)
        self.nutrition_recommendations = NutritionRecommendations()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Dodanie zakładek do interfejsu
        tab_widget = QTabWidget(self)
        tab_widget.addTab(DietPlanCreatorGUI(self.diet_plan_creator), 'Diet Plan Creator')
        tab_widget.addTab(CalorieMonitorGUI(self.calorie_monitor), 'Calorie Monitor')
        tab_widget.addTab(NutrientAnalyzerGUI(self.nutrient_analyzer), 'Nutrient Analyzer')
        tab_widget.addTab(NutritionRecommendationsGUI(self.nutrition_recommendations), 'Nutrition Recommendations')

        layout.addWidget(tab_widget)

        self.setLayout(layout)
        self.setWindowTitle('Diet Planner')

if __name__ == '__main__':
    app = QApplication([])

    diet_planner_gui = DietPlannerGUI()
    diet_planner_gui.show()

    app.exec_()

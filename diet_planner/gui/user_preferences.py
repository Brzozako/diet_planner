# diet_planner/gui/user_preferences.py
from PyQt5.QtWidgets import QMessageBox

class UserPreferences:
    def __init__(self):
        self.goals = {}
        self.user_data = {}
        self.user_info = {}

    def set_goals(self, goals):
        self.goals = goals

    def set_user_data(self, user_data):
        self.user_data = user_data

    def save_to_file(self, file_name='user_info.txt'):
        file_path = file_name
        with open(file_path, 'w') as file:
            file.write(f"Name: {self.user_info['name']}\n")
            file.write(f"Weight: {self.user_info['weight']}\n")
            file.write(f"Diet Plan: {self.user_info['diet_plan']}\n")

    def save_user_info(self, name, weight, diet_plan):
        self.user_info = {'name': name, 'weight': weight, 'diet_plan': diet_plan}
        QMessageBox.information(None, "Zapisano Informacje",
                                f"Zapisano informacje użytkownika:\n{name}, {weight} kg, Plan: {diet_plan}")

    def generate_nutritional_recommendations(self):

        recommendations = "Przykładowe zalecenia żywieniowe"
        QMessageBox.information(None, "Zalecenia Żywieniowe", recommendations)

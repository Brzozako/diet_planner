# diet_planner/gui/meal_plan.py
from PyQt5.QtWidgets import QMessageBox

class MealPlan:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        self.meals.append(meal)

    def edit_meal(self, old_name, new_meal):
        for i, meal in enumerate(self.meals):
            if meal['name'] == old_name:
                self.meals[i] = new_meal
                break

    def delete_meal(self, name):
        self.meals = [meal for meal in self.meals if meal['name'] != name]

    def display_meals(self):
        # Możesz dostosować sposób wyświetlania posiłków, na przykład, w oknie dialogowym
        meal_list = "\n".join([meal['name'] for meal in self.meals])
        QMessageBox.information(None, "Posiłki", f"Aktualne posiłki:\n{meal_list}")

import os
import json

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.categories = set()

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        self.categories.add(category)

    def calculate_budget(self):
        total_expenses = sum(item["amount"] for item in self.expenses)
        remaining_budget = self.income - total_expenses
        return remaining_budget

    def expense_analysis(self):
        analysis = {}
        for category in self.categories:
            category_expenses = [item["amount"] for item in self.expenses if item["category"] == category]
            total_category_expenses = sum(category_expenses)
            analysis[category] = total_category_expenses
        return analysis

    def save_data(self, filename):
        data = {
            "income": self.income,
            "expenses": self.expenses
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.income = data["income"]
                self.expenses = data["expenses"]
        except FileNotFoundError:
            print("Data file not found. Starting with a clean slate.")

    def clear_data(self, filename):
        self.income = 0
        self.expenses = []
        self.categories = set()
        self.save_data(filename)
        print("All past data has been cleared.")

if __name__ == "__main__":
    tracker = BudgetTracker()
    data_filename = "budget_data.json"
    tracker.load_data(data_filename)

    while True:
        print("Budget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Expense Analysis")
        print("5. Clear All Data and Start Fresh")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            tracker.add_income(amount)
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(category, amount)
        elif choice == "3":
            remaining_budget = tracker.calculate_budget()
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            analysis = tracker.expense_analysis()
            print("Expense Analysis:")
            for category, total_expense in analysis.items():
                print(f"{category}: ${total_expense}")
        elif choice == "5":
            tracker.clear_data(data_filename)
        elif choice == "6":
            tracker.save_data(data_filename)
            print("Exiting")
            break
        else:
            print("Invalid choice. Please choose another option.")

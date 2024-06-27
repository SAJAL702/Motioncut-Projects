class Expense:
    def _init_(self, date, category, amount, notes=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.notes = notes

class ExpenseTracker:
    def _init_(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Date\t\tCategory\tAmount\tNotes")
            for expense in self.expenses:
                print(f"{expense.date}\t{expense.category}\t\t{expense.amount}\t{expense.notes}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total expenses: {total}")

# Example usage

tracker = ExpenseTracker()
while True:
        
    print("\nExpense Tracker Menu:")   
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
       date = input("Enter date (YYYY-MM-DD): ")
       category = input("Enter category: ")
       amount = float(input("Enter amount: "))
       notes = input("Enter notes (optional): ")
       expense = Expense(date, category, amount, notes)
       tracker.add_expense(expense)

    elif choice == '2':
       tracker.view_expenses()

    elif choice == '3':
       tracker.total_expenses()

    elif choice == '4':
       print("Exiting...")
       break

    else:
       print("Invalid choice. Please enter a valid option.")
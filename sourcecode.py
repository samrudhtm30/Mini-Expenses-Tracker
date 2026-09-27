from tabulate import tabulate
expenses=[]
def add_expense(expense):
    date=input("Enter the date of the expense (DD-MM-YYYY): ")
    category=input("Enter the category of the expense: ")
    description=input("Enter a description of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    expense_entry = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense_entry)  
    while True:
        try:
            amount=float(input("Enter the amount: "))
            if amount<=0:
                print("Amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expenses:")
    # for expense in expenses:
    print(tabulate(expenses,headers="keys", tablefmt='grid'))

def category_summary():
    if not expenses:
        print("No expenses recorded.")
        return
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    print("Category Summary:")
    for category, total in category_totals.items():
        print(f"Category: {category}, Total Amount: {total}")

def calculate_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}")

def search_expenses_by_category():
    if not expenses:
        print("No expenses recorded.")
        return
    category = input("Enter the category to search for: ")
    found_expenses = [expense for expense in expenses if expense['category'].lower() == category.lower()]
    if not found_expenses:
        print(f"No expenses found for category '{category}'.")
        return
    print(f"Expenses for category '{category}':")
    for expense in found_expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")

def delete_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    display_expenses()
    try:
        index = int(input("Enter the index of the expense to delete (starting from 0): "))
        if 0 <= index < len(expenses):
            deleted_expense = expenses.pop(index)
            print(f"Deleted expense: Date: {deleted_expense['date']}, Category: {deleted_expense['category']}, Description: {deleted_expense['description']}, Amount: {deleted_expense['amount']}")
        else:
            print("Invalid index. No expense deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Category Summary")
        print("4. Calculate Total Expenses")
        print("5. Search Expenses by Category")
        print("6. Delete Expense")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            calculate_total_expenses()
        elif choice == '5':
            search_expenses_by_category()
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            

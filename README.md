# Mini-Expenses-Tracker
# Expense Tracker
It is a Python program designed for the command line which allows you to keep track of your expenses and look at them either by category or in total.

## Features
- Include an expense by giving it a date, a category, a description, and an amount.
- Show the recorded expenses in a table with a formatted layout.
- Provide a summary of spending according to category.
- Calculate total expenses.
- You can search the expenses by category in a case-insensitive manner.
Remove an expense by using its list index.
- Check that numbers and menu selections are correct.

## Technologies and tools
- Python 3
The formatted tables can be obtained using [`tabulate`](https://pypi.org/project/tabulate/).
- A terminal or command prompt

## Install and run
1. If Python 3 has not already been installed, then install it.
2. Save the program into a file called `expense_tracker.py`.
3. Install the dependency from a terminal:
   ```bash
   python -m pip install tabulate
   ```
4. To do this, run the program from the directory in which the file is located:
   ```bash
   python expense_tracker.py
   ```

   On certain systems, use `python3` instead of `python`.

## Using the program
Choose an option from the menu:
To add an expense, you must enter the date using the DD-MM-YYYY format, specify a category, provide a description, and enter an amount.
- Display Expenses — present all the expenses that have been recorded in a table.
– Give the total amount for each category.
— Calculate the total of all the amounts that have been recorded.
5. **Search Expenses by Category** – locate the expenses that correspond to a category, without regard to letter case.
6. **Delete Expense** — an expense can be removed by referring to its position in the displayed list (the prompt makes use of a zero-based index).
7. **Exit** — terminate the program.

## Testing instructions
The program can be checked manually from the menu:

1. Begin the program and, before carrying out any other action, choose **Display Expenses'; the program should indicate that no expenses have been recorded.
2. Include two expenses, with two of them belonging to the same category but being different in amount.
3. Show the expenses and check their dates, categories, descriptions, and amounts.
4. Make sure that the category summary and total match the amounts that have been entered.
Look up a category using a different capitalization and then search for a category which has no expenses matching it.
6. Use a valid index to remove an expense and then attempt to delete an expense with an out-of-range index and non-numeric input.
7. Attempt to select invalid menu options and make sure that the programme asks you again; then choose Exit to end it.

## Screenshots
![Add expenses](<def expenses.png>)
![Display expenses](<def display expenses.png>)
![Category Summary](<def category summary.png>)
![Calculate total expenses](<def calculate total expenses.png>)
![search Expenses by category ](<def search expenses by category.png>)
![Delete expenses](<def delete expenses.png>)
![While true](<while true.png>)

## Screeshots of outputs 
![Add expenses output](<add expenses output.png>) 
![Calculate the summary ](<calculate the summary output.png>)
![calculate total expenses](<calculate total expenses output.png>)
![display expenses](<display expenses output.png>)
![Search by category](<search by category output.png>)
![delete the expenses](<delete the expenses output.png>)

## Notes
The expenses are stored in the program's in-memory list and are deleted when the program exits; this version of the program does not save the data to a file or database. The prompt for the amount in the provided code should remain within the add-expense process so that the amount which has been validated is the one that is stored together with the expense.

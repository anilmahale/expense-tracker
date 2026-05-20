expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    expenses.append(amount)
    print("Expense added!")

def show_total():
    print("Total expense:", sum(expenses))

def save_to_file():
    with open("expenses.txt", "w") as f:
        for e in expenses:
            f.write(str(e) + "\n")

while True:
    print("\n1. Add Expense\n2. Show Total\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_total()
    elif choice == "3":
        break
Feature work

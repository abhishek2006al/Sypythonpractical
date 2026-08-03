print("=============Monthly Expenses Tracker===========")
n=int(input("Enter total expanses:"))

expenses=[]
total=0
for i in range(n):
    amount=float(input(f"Enter the expense {i+1}:"))
    expenses.append(amount)
    total += amount

while True:
    print("*****************Expenses Tracker Menu*********************")
    print("1.Show all expenses")
    print("2.Show total of all expenses")
    print("3.Add new expenses")
    print("4.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        for i in range(len(expenses)):
            print(f"Expenses{i+1}:{expenses[i]}")

    elif choice==2:
        print("Total Monthly Expenses is:",total)

    elif choice==3:
        new_expenses=float(input("Enter new expenses:"))
        expenses.append(new_expenses) 
        total += amount
        print("Expenses added succesfully")

    elif choice==4:
        print("Thank you for using Monthly Expenses Tracker ")
        break

    else:
        print("Invalid choice! Please try again")

                 
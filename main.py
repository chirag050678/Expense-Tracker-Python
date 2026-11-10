#Create a console based Expence Tracker program in Python that allows the user to record the user to record daily experses and view summaries like total spending.

Expenses = [] #lists of all expencses details in form of the dictionary 

print("Welcome User ")
while True:
    print("~~~~Menu~~~~")
    print("1. Add Expenses ")
    print("2. Check Expenses ")
    print("3. Total the Expenses ")
    print("4. Exit")

    choice = int (input("Enter your choice : "))

#Add Expenses
    if (choice ==1):
        Date = input("Enter the Date of Expense in the Formet DD-MM-YYYY : ")
        Cateogory = input("Enter the Type of Expense : ")
        Description = input("Enter the description of the Expense : ")
        Amount = float (input("Enter the Amount of Expense : "))

        expense= {
            "Date": Date,
            "Cateogory" : Cateogory,
            "Description" : Description,
            "Amount" : Amount
        }

        Expenses.append(expense)
        print("\n Expenses Added Successfully ")

#2. View All Expenses 
    elif (choice == 2):
        if (len(Expenses)==0):
            print("Expense is Zero ")
        else :
            print("Your Expenses are : ")
            count = 1
            for i in Expenses:
                print(f"{count}. -> {i ["date"]}, {i["cateogory"]}, {i["Description"]}, {i["Amount"]}")

#3. View Total Spending
    elif (choice == 3):
        total = 0
        for i in Expenses:
            total = total + i["Amount"]
        print("Total Amount : ", total)

#Exit
    elif(choice == 4):
        print("Completed the Expense Record ")
        break

    else:
        print("Invalid Choice")

    
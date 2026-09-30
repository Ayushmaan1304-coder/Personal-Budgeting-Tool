import json
def make_budget(user_id):
    with open("src/user_data.json") as file:
        user=json.load(file)
        
    income=user[user_id]["Income sources"]
    total_income=0
    for source,details in income.items():
        total_income+=int(details["Monthly Income"])
    print("Total Month Income:",total_income)
    expenses = user[user_id]["Expenses"]
    total_expenses = sum(expenses.values())
    print("Total Monthly Expenses:", total_expenses)

    remaining_amount= (total_income)-(total_expenses)
    print(f"{user_id},Your remaining amount that is {remaining_amount} can be used for budgeting")

    name="Monthly Budget"
    print(name.center(45,"*"))
    print("Monthly Income       :",total_income)
    print("Monthly Expenses     :",total_expenses)
    print("Remaining Amount     :",remaining_amount)
    if total_income>0:
        savings_percentage=(remaining_amount/total_income)*100
        print(f"Savings percentage  :{savings_percentage}%")

        print("Your Savings should be 25 % of your income")
        if remaining_amount < 0:
            print("This is an alarming situation. You need to cut down your expenses.")

        elif savings_percentage >= 25:
            print("Good! You are meeting your savings target.")

        else:
            print("This is an alert situation. You need to save more.")
    else:
        print("Income must be greater than zero to create a budget")

    print("*"*45)  






      


    

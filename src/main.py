import json
import user_regestration
import expense
import income_sources
import budget

print("Hi Sir, I am your Personal Budgeting tool")
a=input("Are you an existing user?")
if (a.lower()=="yes"):
    user_id=input("Enter your user id:")
    with open("src/user_data.json","r") as file:
        user=json.load(file)
    if not user[user_id]["Income sources"]:
        income_sources.income_calculator(user_id)
    if not user[user_id]["Expenses"]:
        expense.expense_calculator(user_id)
else:
    print("So Now you have to register yourself first")
    user_id=user_regestration.user_regestration_system()
    income_sources.income_calculator(user_id)
    expense.expense_calculator(user_id)

budget.make_budget(user_id)

       

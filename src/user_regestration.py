import json
def user_regestration_system():
    with open("src/user_data.json","r") as file:
        user=json.load(file)
    new_user_id=f"user{len(user)+1}"      
    user_id={
    "name":input("Enter your name:"),
    "age": input("Enter your age:"),
    "occupation":input("Enter your occupation:"),
    "Income sources":{},
    "Expenses":{}
    }
    user[new_user_id]=user_id
    with open("src/user_data.json","w") as file:
        json.dump(user,file,indent=3)
    print("Your user id is:", new_user_id, "Everytime use this id to check details about you.") 
    return new_user_id

        


     

        














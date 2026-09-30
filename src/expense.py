import json
def expense_calculator(user_id):
    with open("src/user_data.json","r") as file:
            user=json.load(file)
            
            
    print("ok",user_id,"Now you need to ask some of my questions regarding your expenses:")
    expense_dictionary={}
    b=input("Do you want to add expenses?Answer in \"yes\" or \"no\"")
    if(b=="yes"):
        while (b=="yes"):
                expense_name=input("Enter your expense name:")
                amount=int(input("Enter the amount spent:"))

                more=input("Do you want to add more expense? Answer me in \"yes\" or \"no\"")
                expense_dictionary[expense_name]=amount #Expense Id can be given in future

                if(more=="no"):
                        break
    else:
        print("Awesome! You dont have any expense this month")
    user[user_id]["Expenses"]= expense_dictionary 
    with open("src/user_data.json", "w") as file:
        json.dump(user, file, indent=4) 


       





        
        

        
                

                
    
          

       
       
       
       

    
    
    



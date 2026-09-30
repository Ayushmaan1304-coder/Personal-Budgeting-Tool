import json
from datetime import date,datetime
def income_calculator(user_id):
    with open("src/user_data.json","r") as file:
        user=json.load(file)
    print("Ok",user_id,"Now tell me your different income sources:")
    income_dictionary={}
    while True:
        income_options={"1":"Salary",
                        "2":"Freelancing",
                        #"3":"Bank returns",
                        "3":"Rental income",
                        "4":"Investment income",
                        "5":"Royalty",
                        "6":"Agricultural income",
                        "7": "Pension",
                        "8":"Side Business",
                        "9":"Other"
                        }
        print(income_options)
        a=income_options[input("Enter your number")]
        match a:
            case "Salary":
                print("What is your salary per month?")
                salary=int(input (("Enter your salary:")))
                income_dictionary["Monthly Income"]={"Monthly income":salary}
            case "Freelancing":
                field=input("In what field you are doing freelancing, describe it for further recommendations:")    
                Freelancing=int(input("How much are you able to earn from it per month?"))
                income_dictionary["Freelancing"]={"Field":field,
                                                "Monthly Income":Freelancing}
    
            case "Rental income":
                rent=int(input("Enter your rental income:"))
                income_dictionary["Rental Income"] = {"Monthly Income":rent}
            case "Investment income":
                # # invest={"1":"Stocks", #Later I will be giving options here to user to add which type of investment..
                #         "2":"Real Estate",
                #         "3":"Gold",
                #         "4":"other"}
                income=int(input("Enter your investment income:"))
                income_dictionary["Investment income"]={"Monthly Income":income}
            case "Royalty":
                royalty=input("Enter your royalty source?:")
                royalty_income=int(input("Enter your income from royalties:"))
                income_dictionary["Royalty"] = {
        "Source": royalty,
        "Monthly Income": royalty_income
    }
            case "Agricultural Income":
                agricultural_income=int(input("Enter your agricultural income:")) #Here more information regarding the agricultural land ki jagah and wheat type can and dudration can be taken so that it can be given spereately to agricultural advisor
                income_dictionary["Agricultural Income"] = {"Monthly Income":agricultural_income}  
            case "Pension":
                pension_income=int(input("Enter your pension income:"))
                income_dictionary["Pension"] = {"Monthly Income":pension_income}
            case "Side Business":
                side_business=input("What is your business?:")
                side_business_income=int(input("Enter your income from this side business?:"))
                income_dictionary["Side Business"] = {
        "Business": side_business,
        "Monthly Income": side_business_income
    }
            case "Other":
                
                other_income_sources = []

                while True:
                    other = input("Enter your other source of income: ")
                    other_income_sources.append(other)

                    more = input("Do you want to add another source? (yes/no): ")

                    if more.lower() == "no":
                        break

                print("Your other sources of income are:")
                for number, source in enumerate(other_income_sources, start=1):
                    print(f"{number}) {source}")
                total_other_income=float(input("Enter the total you are earning from all of the above:"))
                income_dictionary["Other"] = {
        "Sources": other_income_sources,
        "Monthly Income": total_other_income
    }
        more=input("Do you want to add more income sources?(yes/no):")
        if more.lower()=="no":
         break            
    user[user_id]["Income sources"]=income_dictionary
    with open("src/user_data.json","w") as file:
        json.dump(user,file,indent=4)   




            
            
        
    

                
            


        
        
        
        
        


                    

                    


                    
                    




                    

                    


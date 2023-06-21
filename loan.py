

# introduction
def assignment():
    print("==========welcome to GTbank============\n")
    user=input("enter your first name: ")
    user2=input("enter your last name: ")
    place_of_work=input("enter place of work: ")
    print("welcome",user,user2,"to GTbank we are here to serve you better please can you state why you are here?")
    print("kindly select why you are here:\n 1 response1\n 2 response2\n 3 response3")
    response= int(input("enter number: "))
# condition for introduction

    if response == 1:
        print("wait for 5 seconds before you proceed to enter your details......")
        print(user,user2,"you may enter your details here")
        
    elif response == 2 :
        print("insert  your card")
    elif response == 3:
        print("visit our customer care centers close to you")
    else:
        print("sorry please select a valid option")
        assignment() 
      
assignment()
# introduction close


# details

def details():
    loan=45
    print("Accessed loan percentage: ",loan,"%")
    current_amount=int(input("Enter your current salary amount: N"))
    total_annual_income=float(current_amount*12) 
    print("total annual income: N ",total_annual_income)
    accessed_loan=float(45/100)
    print("accessed loan: N ",accessed_loan) 
    loan_amount=(accessed_loan)*(total_annual_income)
    print("loan amount per annual income: N ",loan_amount)
    credit_history=float(input("Enter 6 months credit history: "))
    print("6 months credit history:",credit_history)
    granted_deposit_date= 1
    last_deposit_date=int(input("enter when last deposit was made: "))
    granted_loan_collection_date=6
    last_loan_collection_date=int(input("Enter last loan collection date: "))
    granted_loan_repayment=6
    loan_repayment_period=int(input("Enter when loan repayment will be made: "))
    account_operated_type=input("enter account type operated:")
    account1="savings"
    account2="current"
    

    



    
    if current_amount >=int(loan_amount) :
        print("current amount points: +10")

    elif current_amount < int(loan_amount):
        print("current amount points:-10 ")
    else:
        print("sorry you have'nt entered the correct option")
        details()
 
    if credit_history >= loan_amount:
        
        print("6 months credit history points:+10")
    elif credit_history < loan_amount:
        
        print("6 months credit history points:-10")
    else:
        print("not valid")
        details()
 
    
    if last_deposit_date >= granted_deposit_date:
        print("Granted deposit date points: +5 ")

    elif last_deposit_date < granted_deposit_date:

        print("Granted deposit date points: -5 ")
    else:
        print("not valid")
        details()
 
    
    if last_loan_collection_date >= granted_loan_collection_date:
    
        print("Granted loan collection date points: +10 ")

    elif last_loan_collection_date < granted_loan_collection_date:
    
        print("Granted loan collection date points: -10 ")

    else:
        print("not valid")
        details()
 
    
    if loan_repayment_period >= granted_loan_repayment:
    
        print("granted repayment period point: -5")
       
    elif loan_repayment_period > granted_loan_repayment:
        
        print("granted repayment period point: +5")
   
    else:
        print("not valid")
    
    if account_operated_type == account1 :
        
        print("account operated type points: 5 ")
    elif account_operated_type == account2 :
        
        print("account operated type points: 10 ")
    else:
        print("not valid")
        details()
    

details()

grantedscore=30
granteddepositdate_point=int(input("enter granted deposit date point:"))
    
grantedcredithistory_point=int(input("enter granted credit history point:"))
    

grantedloancollection_point=int(input("enter granted loan collection point:"))
    
    
grantedloanrepayment_point=int(input("enter granted loan repayment point:"))
    
    
accountoperatedtype_point=int(input("enter account operated type point:"))

    
totalscore=granteddepositdate_point + grantedcredithistory_point+grantedloancollection_point+grantedloanrepayment_point+accountoperatedtype_point
print("The total client score:" ,totalscore)


if totalscore >= grantedscore:
        print("congratulations loan granted")
elif totalscore < grantedscore:
        print("sorry loan denied")
else:
        print("not valid")
        details()
 
    
   
   

def details():
    loan=45
    print("Accessed loan percentage: ",loan,"%")
    current_amount=int(input("Enter your current salary amount: "))
    total_annual_income=float(current_amount*12) 
    print("total annual income: ",total_annual_income)
    accessed_loan=float(45/100)
    print("accessed loan: ",accessed_loan) 
    loan_amount=(accessed_loan)*(total_annual_income)
    print("loan amount per annual income: ",loan_amount)
    credit_history=float(input("Enter 6 months credit history: "))
    print("6 months credit history:",credit_history)
    granted_deposit_date= 1
    last_deposit_date=(input("enter when last deposit was made: "))
    granted_loan_collection_date=6
    last_loan_collection_date=int(input("Enter last loan collection date: "))
    granted_loan_repayment=6
    
    loan_repayment_period=int(input("Enter when loan repayment will be made: "))
    account_operated_type=input("enter account type operated:")
    account1="savings"
    account2="current"
    grantedscore=30
    

    



    
    if current_amount >=int(loan_amount) :
        answer=0
        answer= answer+10
        print("current amount points:",answer)
    else:
        print("sorry you have'nt entered the correct option")
        
 
    if credit_history >= loan_amount:
        answer=answer+10
        print("6 months credit history points:+10")
    elif credit_history < loan_amount:
        answer=answer-10
        print("6 months credit history points:-10")
    
        
    
    if last_deposit_date >= granted_deposit_date:
        answer=answer+5
        print("Granted deposit date points:",answer)

    elif last_deposit_date < granted_deposit_date:
        answer=answer-5
        print("Granted deposit date points: ",answer)
    else:
        print("not valid")
    
    if last_loan_collection_date >= granted_loan_collection_date:
        answer=answer+10
        print("Granted loan collection date points:",answer)

   
    else:
        print("not valid")
    
    if loan_repayment_period >= granted_loan_repayment:
        answer=answer -5
        print("granted repayment period point:",answer)
       
    elif loan_repayment_period > granted_loan_repayment:
        answer=answer+5
        print("granted repayment period point: ",answer)
   
    else:
        print("not valid")
    
    if account_operated_type == account1 :
        answer=answer+5
        print("account operated type points: ",answer)
    elif account_operated_type == account2 :
        answer=answer+10
        print("account operated type points:  ",answer)
    else:
        print("not valid")
    if answer >= grantedscore:
        print("loan granted")
    elif answer < grantedscore:
        print("loan denied")
    else:
        print("not valid")

        
    

details()


    

    

    
   
   
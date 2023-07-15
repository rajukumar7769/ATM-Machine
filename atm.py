#Python Code For ATM Machine

#Features
#1.pin authentication
#2.withdraw feature
#3.Deposit feature
#4.Balence check

        

def withdraw(remain_bal,with_amount):
    remain_bal= remain_bal-with_amount
    print(with_amount,"is withdraw from your account.")
    print("Remaining Balane after debit:",end="")
    return remain_bal
 
    
def current_balance():
    print("Current Balance is: ",end="")
    return remain_bal

def deposit_balance(remain_bal,deposit_amount):
    remain_bal=remain_bal+deposit_amount
    print("Current Balance after credit: ",end="")
    return remain_bal

print("\n:---------: Welcome Swiss Bank ATM Machine :---------:\n")
print("Insert ATM CARD into Machine\n")
pin_num=int(input("Enter 4-Digit Pin Number : "))
if(pin_num==1234):
    print("\npress 1 for withdraw money")
    print("press 2 for check current balance")
    print("press 3 for deposit balance")
    print("Press 4 to cancel transection\n")
    option=0
    with_amount=0
    remain_bal=10000000
    
    while(option!=4):
        option=int(input("choose your option: ")) 
        print("\n")
        if(option>4):
            print(":--------: Wrong Option :-------:")
        else:
            if(option==1):
                with_amount=int(input("Enter Amount To Withdraw:"))
            
                print(withdraw(remain_bal,with_amount))
                remain_bal=remain_bal-with_amount
                print("\n:---------: Your Transection Is Successful :---------:\n")
         
            if(option==2):
                print(current_balance())
                print("\n:----------: Current Balance :----------:\n")
                
            if(option==3):
                deposit_amount=int(input("Enter Amount To Deposit:"))
                
                print(deposit_balance(remain_bal,deposit_amount))
                remain_bal=remain_bal+deposit_amount
                print("\n:----------: credited Balance :----------:\n")
            
    print("\n:---------: Transection Timeout :----------:\n")
else:
    print("\n:---------: You Enters a wrong pin. Try again :---------:\n")       
        




id = input("Enter your ID: ")

current_account = account[id]

uname = input("Enter your username: ")
pin = input("Enter your pin: ")

if uname == current_account['username'] and pin == current_account['pin']:
    print(f"Current Balance: {current_account['balance']}")
    do = int(input("""
    [1] Withdraw
    [2] Deposit
    [3] Cancel
                   
    Please enter your choice: """))
    
    if do == 1:
        wit_num = int(input("How much would you like to withdraw?"))
        remaining_bal = calc("-", current_account['balance'], wit_num)
        account[id]['balance'] = remaining_bal

    elif do == 2:
        dep_num = int(input("How much would you like to deposit?"))
        remaining_bal = calc("+", current_account['balance'], dep_num )
        account[id]['balance'] = remaining_bal
        
    else:
        print("Thank you for using.")

else:
    print("Invalid username or pin")
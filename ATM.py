def check_balance(bal):
    return bal
def deposite(amount,bal):
    if amount > 0:
        bal += amount
        print("\nSuccessfully deposited")
    else:
        print("\nInvalid deposit amount.")
        return bal
    return bal
def withdraw(amount,bal):
    if amount > bal:
        print("\nInsufficient amount")
    elif amount <= 0:
        print("\ncheck amount you want to withdraw")
    else:
        bal -= amount
        print("\nAmount withdrawed")
        return bal

bal = 10000
while True:
    print("\n1.Check Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 4:
        print("\nTHANK YOU")
        break
    elif choice in [1,2,3]:
        if choice == 1:
            print("\nYour Balance is:",check_balance(bal))
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            bal = deposite(amount,bal)
        elif choice == 3:
            amount =int(input("Enter amount to withdraw: "))
            bal = withdraw(amount,bal)
        else:
            print("\n INVALID CHOICE")
    else:
        print("\n INVALID CHOICE")
        break

import time

print("Please Insert Your Card")

time.sleep(5)

pas = 1234
balance = 10000
pin = int(input("Enter Your Pin: "))

if pin == pas:
    while True:
        print("\n 1 => Balance\n 2 => Withdraw\n 3 => Deposit\n 4 => Exit\n")
        try:
            op = int(input("Please Enter Your Choice: "))
        except ValueError:
            print("Please Enter a Valid Option")
            continue

        if op == 1:
            print(f"Your Current Balance is {balance}")
            print("***************************************************")
        
        elif op == 2:
            withdraw = int(input("Please Enter Withdrawal Amount: "))
            if withdraw <= balance:
                balance -= withdraw
                print(f"{withdraw} is debited from your account.")
                print(f"Your Current Balance is {balance}")
            else:
                print("Insufficient Balance")
            print("***************************************************")
        
        elif op == 3:
            deposit = int(input("Please Enter Deposit Amount: "))
            balance += deposit
            print(f"{deposit} is credited to your account.")
            print(f"Your Current Balance is {balance}")
            print("***************************************************")
        
        elif op == 4:
            print("Thank you for using the ATM. Have a nice day!")
            break
        
        else:
            print("Invalid Option. Please Try Again.")
else:
    print("Entered Pin Is Incorrect")

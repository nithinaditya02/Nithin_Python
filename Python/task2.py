

#conditional statements


#if
#if-else
#if-elif-else
#nested if


# if program example
# if 10>5:
#     print("10 is greater than 5")



# if-else program example
# age=23
# if age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")



# if-elif-else program example

# marks=85
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# else:
#     print("Grade C")




#TASK - ATM Simulator 1234
correct_pin = 1234
balance = 10000

pin = int(input("Enter your 4 digit pin: "))

if pin == correct_pin:
    print("Welcome to the ATM")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Transfer Money")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is: {balance}")

    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than ₹0")
        elif amount <= balance:
            balance = balance - amount
            print(f"Withdrawal successful. Your new balance is: {balance}")
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter the amount to deposit: "))

        if amount <= 0:
            print("Invalid amount. Please enter a positive amount.")1234
        else:
            balance = balance + amount
            print(f"Deposit successful. Your new balance is: {balance}")

    elif choice == 4:
        account_number=int(input("Enter the account number to transfer money:"))
        transfer_amount=int(input("Enter the amount to transfer:"))
        if transfer_amount > balance:
            print("Insufficient balance for transfer.")
        else:
            balance = balance-transfer_amount
            print(f"Transfer of {transfer_amount} to account {account_number} successful.")

    elif choice == 5:
            print("Thank you for using the ATM.")
    else:
        print("Invalid choice")

else:
    print("Invalid PIN. Please try again")
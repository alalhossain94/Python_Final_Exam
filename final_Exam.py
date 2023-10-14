import random
class User:
    def __init__(self,name,email,address,accountNumber,AccountType) -> None:
        self.name=name
        self.email=email 
        self.address=address
        self.accountNumber=accountNumber
        self.accountType=AccountType
        self.balance=0
        self.transactions=[]
        self.loans_taken=0

    def deposit(self,amount):
        if amount >=0:
            self.balance +=amount
            self.transactions.append(f"Deposited amount: ${amount}")
        else:
            print(f"Invalid deposit amount")

    def withdraw(self,amount):
        if amount >=0 and amount <= self.balance:
            self.balance -=amount
            print(f"\nWithdrew amount: ${amount}. New balance: ${self.balance}")
            self.transactions.append(f"Withdrew amount: ${amount}")
        else:
            print(f"Withdrawal amount exceeded")
              
    def check_available_balance(self):
        return self.balance
    
    def check_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)
         
    def take_loan(self,amount):
        if not bank.loan_enabled:
            print("Loans are currently unavailabe")
        elif self.loans_taken < 2:
            self.loans_taken += 1
            self.balance += amount
            loan=Loan(self,amount)
            bank.loans.append(loan)
        else:
            print("You have already taken the max number of loans.")

    def transfer_amount(self, recipient,amount):
        if recipient in bank.users:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transactions.append(f"Transferred amount: &{amount} to {recipient.name}")
                recipient.transactions.append(f"Received amount: ${amount} from {self.name}")
            else:
                print("Balance not sufficient for transfer.")
        else:
            print("Recipient's account does not exist")


class Bank():
    def __init__(self) -> None:
        self.users=[]
        self.loans=[]
        self.loan_enabled=True

    def create_account(self,name,email,address,accountType):
        accountNumber=random.randint(2000,9000)
        user=User(name,email,address,accountNumber,accountType)
        self.users.append(user)
        return user

    def delete_account(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f"The account of {user.name} with account number {user.accountNumber} has been deleted!")
        else:
            print("Account user not found.")
    
    def user_accounts_list(self):
        for user in self.users:
            print("----------------------------------------------------------")
            print(f"Account holder's name: {user.name}\nAccount Number: {user.accountNumber}\nEmail address: {user.email}\nAccount balance: ${user.balance} ")
            print("----------------------------------------------------------")

    def total_available_balance_of_bank(self):
        total=0
        for user in self.users:
            total += user.balance
        return total

    def total_loan_amount(self):
        total=0
        for loan in self.loans:
            total += loan.amount
        return total

    def toggle_switch_loan_feature(self):
        if self.loan_enabled:
            self.loan_enabled=False
        else:
            self.loan_enabled=True

    def is_bankrupt(self):
        total_balance=self.total_available_balance_of_bank()
        return total_balance < 0

class Loan:
    def __init__(self,user,amount) -> None:
        self.user=user
        self.amount=amount
      
bank=Bank()

while True:
    print("\n----------------------")
    print("Bank Management System")
    print("----------------------")
    print("1. User Tasks")
    print("2. Admin Tasks")
    print("3. Exit")
    choice=input("\nSelect an option: ")
    if choice== "1":
        print("\n----------")
        print("User Tasks")
        print("----------")
        accountNumber=int(input("Enter your account number: "))
        currentUser=None
        for user in bank.users:
            if user.accountNumber == accountNumber:
                currentUser=user
                break
                
        if user:
            print(f"\n---->>Welcome, {user.name}<<----!")
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Check Transaction History")
                print("5. Take Loan")
                print("6. Transfer Money to Another Account")
                print("7. Back to Main Menu")
                user_choice=input("\nSelect an option: ")
                if user_choice== "1":
                    deposit_amount=int(input("Enter the amount to deposit: $"))
                    user.deposit(deposit_amount)
                    print(f"New balance: ${user.check_available_balance()}")
                
                elif user_choice == "2":
                    withdraw_amount=int(input("Enter the amount to withdraw: $"))
                    user.withdraw(withdraw_amount)

                elif user_choice == "3":
                    print(f"Availabl Balance: ${user.check_available_balance()}")

                elif user_choice == "4":
                    print("---------Transaction History---------")
                    user.check_transaction_history()

                elif user_choice == "5":
                    loan_amount=int(input("Enter the loan amount: $"))
                    user.take_loan(loan_amount)
                    print(f"New balance: ${user.check_available_balance()}")

                elif user_choice == "6":
                    recipient_account_number=int(input("Enter the recipient's account number: "))
                    recipient=None
                    for r in bank.users:
                        if r.accountNumber == recipient_account_number:
                            recipient=r
                            break
                    if recipient:
                        amount= int(input(f"Enter the amount to transfer to {recipient.name}: $"))
                        user.transfer_amount(recipient,amount)
                    else:
                        print("Recipient's account does not exist")
               
                elif user_choice == "7":
                    break
        else:
            print("Acount not found")



    elif choice== "2":
        print("\n-----------")
        print("Admin Tasks")
        print("-----------")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. List of Accounts ")
        print("4. Total Available Balance")
        print("5. Total Loan Amount")
        print("6. Toggle Switch Loan Feature")
        print("7. Check Bankruptcy")
        print("8. Back to Main Menu")
        admin_choice= input("Select an option: ")

        if admin_choice == "1":
            name=input("Enter Your Name: ")
            email=input("Enter Your Email: ")
            address=input("Enter Your Address: ")
            accountType=input("Enter the Account Type (Savings or Current): ")
            user=bank.create_account(name,email,address,accountType)
            print(f"Your account is created with account number: {user.accountNumber}")
        elif admin_choice == "2":
            accountNumber=int(input("Enter the account number to detele: "))
            for user in bank.users:
                if user.accountNumber == accountNumber:
                    currentUser=user
                    break
            if user:
                bank.delete_account(user)

        elif admin_choice == "3":
            print("---------User Accounts List---------")
            bank.user_accounts_list()
        
        elif admin_choice == "4":
            print(f"Total available balance in the bank: ${bank.total_available_balance_of_bank()}")

        elif admin_choice == "5":
            print(f"Total loan balance in the bank: ${bank.total_loan_amount()}")

        elif admin_choice == "6":
            bank.toggle_switch_loan_feature()
            if bank.loan_enabled:
                status= "enabled"
            else:
                status= "disabled"
                print(f"Right now, Loan feature is {status}")

        elif admin_choice == "7":
            if bank.is_bankrupt():
                print("The bank is bankrupt!")
            else:
                print("The bank is not bankrupt.")

            
        elif admin_choice == "8":
            pass
    elif choice== "3":
        print("Exit the Bank Management System.")
    
    else:
        print("Invalid Option.Kindly try again")
    


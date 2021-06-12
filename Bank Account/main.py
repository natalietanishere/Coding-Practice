from random import randint
class account:
 
  def create_account():
    return 0
 
  def authenticate():
    return 0
 
  def withdrawal():
    return 0 
 
  def deposit():
    return 0
 
  def display_balance():
    return 0 
class saving_account(account): #more convenient to make 2 classes & easier to read
 
  def __init__(self):
    self.saving_accounts = {"11111":["hemil", 1]} 
    #creates dictionary, which has {}, key, and value
    #"hemil" is a placeholder
    #__init__ is a constructor, which is kind of like an empty list
  def create_account(self,name,initial_deposit): #not using name 
    self.account_number = randint(10000,99999) #int means integer
    self.saving_accounts[self.account_number] = [name,initial_deposit] 
    #refers to account #, name, and money
    print("Your account was created! Your account number is"+ self.account_number +".")
  
  def authenticate(self,name,account_number): #tests to confirm account
    if account_number in self.saving_accounts.key():#refers to dictionary for account numbers
      if self.saving_accounts[account_number][0] == name:
        print("Authentication successful.")
        self.account_number = account_number # refers to account number variable
 
  def withdrawl(self,withdrawal_amount):
    if withdrawal_amount > self.saving_accounts[self.account_number][1]:
       print("Insufficient balance.")
    else:
      self.saving_accounts[self.account_number][1] -= withdrawal_amount
      print("Withdrawal successful.")
  
  def deposit(self, deposit_amount): #will create withdrawal function
    self.saving_accounts[self.account_number][1] += deposit_amount #adds deposit value
    print("Deposit successful.")
    self.display_balance(self.account_number)
  
  def display_balance(self,account_number): #prints information
    print("Available balance:" +  self.saving_accounts[self.account_number][1]) 
  
  while True:
    print("Enter 1 to make an account.")
    print("Enter 2 to open an existing account. ")
    print("Enter 3 to exit. ")
    user = raw_input()
    if user == 1:
      name = input("What is your name? ")
      initial_deposit = input("Enter the amount you are depositing. ")
      saving_account.create_account(name,initial_deposit)#refers to create_account function
    if user == 2:
       name = input("Name: ")
       account_number = input("Account Number: ")
       authentication_status = saving_account.authenticate(name,account_number)
       if authentication_status is True:
         while True:
           print("Enter 1 to deposit, Enter 2 to withdrawal, Enter 3 to display balance, Enter 4 to exit.  ")
           choice = raw_input()
           if choice == 1:
             deposit_amount = input("Deposit Amount: ")
             saving_account.deposit(deposit_amount)
           if choice == 2:
              withdrawal_amount = input("Withdrawal Amount: ")
              saving_account.withdrawal(withdrawal_amount)
           if choice == 3:
              saving_account.display_balance(account_number)
           if choice == 4:
             break
    if user == 3:
       quit()
           
       
  
    
    
    
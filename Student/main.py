STUDENT_NAME = []
STUDENT_ROLL_NUMBER = []
STUDENT_ADDRESS = []
STUDENT_EMAIL = []
STUDENT_AGE = []
STUDENT_MOBILE_NUMBER = []
STUDENT_CLASS = []

# add, delete, update, display 
class student_management_system:
  @staticmethod
  def addition():
    name_ask = input("What is your name? ").lower()
    STUDENT_NAME.append(name_ask)

    roll_ask = int(input("What is your roll number? "))
    STUDENT_ROLL_NUMBER.append(roll_ask)

    address_ask = input("What is your address? ").lower()
    STUDENT_ADDRESS.append(address_ask)

    email_ask = input("What is your email? ").lower()
    STUDENT_EMAIL.append(email_ask)

    age_ask = input("What is your age? ").lower()
    STUDENT_AGE.append(age_ask)

    number_ask = input("What is your phone number? ").lower()
    if len(number_ask) < 10:
      print("Invalid number.")
    elif len(number_ask) > 10:
      print("Invalid number.")
    else:
      STUDENT_MOBILE_NUMBER.append(number_ask)
    
    class_ask = input("What is your class?").lower()
    STUDENT_CLASS.append(class_ask)
  @staticmethod
  def delete():
    if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0 and len(STUDENT_AGE) == 0 and len(STUDENT_MOBILE_NUMBER) == 0 and len(STUDENT_CLASS) == 0:
      print("There is nothing to delete.")
    
    else:
      roll_input = int(input("What is your roll number?"))
      locate = STUDENT_ROLL_NUMBER.index(roll_input)
      STUDENT_NAME.remove(STUDENT_NAME[locate])
      STUDENT_ROLL_NUMBER.remove(STUDENT_ROLL_NUMBER[locate])
      STUDENT_ADDRESS.remove(STUDENT_ADDRESS[locate])
      STUDENT_EMAIL.remove(STUDENT_EMAIL[locate])
      STUDENT_AGE.remove(STUDENT_AGE[locate])
      STUDENT_MOBILE_NUMBER.remove(STUDENT_MOBILE_NUMBER[locate])
      STUDENT_CLASS.remove(STUDENT_CLASS[locate])
      print("Delete successful")
  @staticmethod
  def update():
    if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0 and len(STUDENT_AGE) == 0 and len(STUDENT_MOBILE_NUMBER) == 0 and len(STUDENT_CLASS) == 0:
       print("There is nothing to display.")
    else:
      attribute = input("What attribute do you want to update?").lower()
      if attribute == "name":
        OLD_NAME = str(input("Enter 'old name' :")).lower()
        LOC_NAME = STUDENT_NAME.index(OLD_NAME)
        
        NEW_NAME =str(input("Enter 'new name'")).lower()
        STUDENT_NAME[LOC_NAME] = NEW_NAME
        print("\t Name updated successfully.")
        print("\n")
        
      if attribute == "roll number":
        OLD_ROLL_NUMBER = int(input("Enter 'old roll number' :")).lower()
        LOC_ROLL_NUMBER = STUDENT_ROLL_NUMBER.index(OLD_ROLL_NUMBER)
        
        NEW_ROLL_NUMBER = int(input("Enter 'new name'")).lower()
        STUDENT_ROLL_NUMBER[LOC_ROLL_NUMBER] = NEW_ROLL_NUMBER
        print("\t Roll number updated successfully.")
        print("\n")       

      if attribute == "age":
        OLD_AGE = int(input("Enter 'old age' :")).lower()
        LOC_AGE = STUDENT_AGE.index(OLD_AGE)
        
        NEW_AGE = int(input("Enter 'new age'")).lower()
        STUDENT_AGE[LOC_AGE] = NEW_AGE
        print("\t Age updated successfully.")
        print("\n")
      
      if attribute == "class":
        OLD_CLASS = str(input("Enter 'old class' :")).lower()
        LOC_CLASS = STUDENT_CLASS.index(OLD_CLASS)
        
        NEW_CLASS = str(input("Enter 'new class'")).lower()
        STUDENT_CLASS[LOC_CLASS] = NEW_CLASS
        print("\t Class updated successfully.")
        print("\n")
      
      if attribute == "email":
        OLD_EMAIL = str(input("Enter 'old email' :")).lower()
        LOC_EMAIL = STUDENT_EMAIL.index(OLD_EMAIL)
        
        NEW_EMAIL =str(input("Enter 'new email'")).lower()
        STUDENT_EMAIL[LOC_EMAIL] = NEW_EMAIL
        print("\t Email updated successfully.")
        print("\n")

      if attribute == "address":
        OLD_ADDRESS = str(input("Enter 'old address' :")).lower()
        LOC_ADDRESS = STUDENT_ADDRESS.index(OLD_ADDRESS)
        
        NEW_ADDRESS =str(input("Enter 'new address'")).lower()
        STUDENT_ADDRESS[LOC_ADDRESS] = NEW_ADDRESS
        print("\t Address updated successfully.")
        print("\n")

      if attribute == "phone number":
        OLD_MOBILE_NUMBER = str(input("Enter 'old phone number' :")).lower() 
        LOC_MOBILE_NUMBER = STUDENT_MOBILE_NUMBER.index(OLD_MOBILE_NUMBER)
        
        NEW_MOBILE_NUMBER =str(input("Enter 'new phone number'")).lower()
        if len(OLD_MOBILE_NUMBER) < 10:
          print("Invalid number.")
        elif len(NEW_MOBILE_NUMBER) < 10:
          print("Invalid number.")
        else:
          STUDENT_MOBILE_NUMBER[LOC_MOBILE_NUMBER] = NEW_MOBILE_NUMBER
          print("\t Phone number updated successfully.")
          print("\n")
  @staticmethod
  def display():
    if len(STUDENT_NAME) == 0 and len(STUDENT_ROLL_NUMBER) == 0 and len(STUDENT_ADDRESS) == 0 and len(STUDENT_EMAIL) == 0 and len(STUDENT_AGE) == 0 and len(STUDENT_MOBILE_NUMBER) == 0 and len(STUDENT_CLASS) == 0:
       print("There is nothing to display.")
    else:
      print(STUDENT_NAME)
      print(STUDENT_ROLL_NUMBER)
      print(STUDENT_ADDRESS)
      print(STUDENT_EMAIL)
      print(STUDENT_AGE)
      print(STUDENT_MOBILE_NUMBER)
      print(STUDENT_CLASS)


sms = student_management_system() 
      # https://www.geeksforgeeks.org/__name__-special-variable-python/ 
if __name__ == "__main__": 
  
  while True:
    print("PRESS 1 : TO ADD STUDENT INFORMATION.")
    print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
    print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")
    print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")
    print("PRESS 5 : TO EXIT SYSTEM.")
    entry = int(input("Which one would you like to do?"))
    if entry == 1:
      sms.addition()
    elif entry == 2:
      sms.delete()
    elif entry == 3:
      sms.update()
    elif entry == 4:
      sms.display()
    elif entry == 5:
      break


      # we are essentially done with the application, we'll a brief look at it next week whether it works on not more. next week, we'll have another program 

      # seems to work, we may need to fix some of the 'visual parts' 

      # i'll see you next week 
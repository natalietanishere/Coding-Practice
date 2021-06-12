import random 
#ask user to give leg (how long a password is) via an integer 
#do sampling
leg = int(input("How long is your password?"))
alpha = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
sam = "".join(random.sample(alpha, leg)) #sampling input
print(sam)
import string
import random

character = list("string.ascii_letters"+string.digits+"!@#$%^&*()")
random.shuffle(character)

password= []
length_psd = int(input("please enter the length of your password "))
for x in range(length_psd):
    password.append(random.choice(character))

output = "".join(password) 
print(output)
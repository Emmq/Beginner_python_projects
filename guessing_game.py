import random
print("welcome to this guess game")
num_range = input("please enter a number ")
if num_range.isdigit():
    num_range= int(num_range)
    if num_range <= 0:
        print("please enter a lager number next time")
        quit()
else:
    print("please enter a digit next time")
    quit()
count = 0
while True:
    count +=1
    random_number = random.randint(0,num_range)
    guess= input("make a guess ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please enter a valid number")
        continue
    print(random_number)

    if guess == random_number:
        print("you got it right")
        print("after", count ,"guesses")
        break
    else:
        print("you got it wrong")
        continue
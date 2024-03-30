import random

target = random.randint(1,100)
#print(target)

while True:
    user = (input("Enter a number or Q : "))
    if user == "Q":
        break
    user = int(user)
    if (user == target):
        print("You Won the challange by guessing the correct number - chocolate gift", user)
        break
    elif (user < target):
        print("Your guess is small, try a big number. ", user)
    else:
        print("Your guess is big, try a small number. ", user)
    
print("Game Over Dude!!!! ")
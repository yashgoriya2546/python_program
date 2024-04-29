import random
print("0.snake,1.water,2.gun")

def game(comp,user):
    if comp == user:
        return 0
    elif comp == 0 and user == 1:
        return -1
    elif comp == 1 and user == 2:
        return -1
    elif comp == 2 and user == 0:
        return -1
    else:
        return 1

useres = int(input("Enter a number=>"))
computer = random.randint(0,2)

print("user choice=>",useres)
print("AI choice=>",computer)

score = game(computer,useres)

if score == 0:
    print("game is draw",score)
elif score == -1:
    print("you loss",score)
else:
    print("you won",score)


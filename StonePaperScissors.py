import random
opt = ['scissors', 'stone', 'paper']
z = random.choice(opt) 
y = input("Please type 'stone', 'paper' or 'scissors'. ")
print("computer's choice",z)
if z == 'scissors':
    if y == 'paper':
        print("Oops! Better luck next time")
    elif y == 'scissors':
        print("It's a tie")
    elif y == 'stone':
        print("Yay! You won!")
    else:
        print("Enter a valid option!")

if z == 'stone':
    if y == 'paper':
        print("Yay! You won!")
    elif y == 'stone':
        print("It's a tie")
    elif y == 'scissors':
        print("Oops! Better luck next time")
    else:
        print("Enter a valid option!")

if z == 'paper':
    if y == 'scissors':
        print("Yay! You won!")
    elif y == 'paper':
        print("It's a tie")
    elif y == 'stone':
        print("Oops! Better luck next time")
    else:
        print("Enter a valid option!")

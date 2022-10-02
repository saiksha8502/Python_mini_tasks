import random
n=random.randint(10,20)
flag=False
for i in range(1,4):
    print("Guess the number",i)
    g=int(input("Enter your guess b/w 10 and 20"))
    if g==n:
        flag=True
        print("Correct!!")
        break
    elif g>n:
        print("Your guess is greater than the number")
    else:
        print("Your guess is less than the number")
if flag==false:
    print("Sorry!Better luck next time!")
else:
    print("Well Done")
import random

print ("rock,paper,scisser")

a=input("vared kon :")

b=['rock','paper','scisser']

c=random.choice(b)

print()

if a == c:
    print("no one won /n bot was{}".format(c))
elif a =="rock":
    if c =="paper":
        print("you lost /n bot is paper")
    elif c == "scisser":
        print("you one /n bot is scisser")

elif a =="paper":
    if c =="rock":
        print("you one /n bot is rock")
    elif c =="scisser":
        print("you lost /n bot is scisser")
elif a =="scisser":
    if c =="paper":
        print("you one /n bot is paper")
    elif c == "rock":
        print("you lost /n bot is rock")
'''-1=R   0=P  1=Sc'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter choice:")
youdict={"r":-1,"p":0,"Sc":1}
reversedict={-1:"Rock", 0:"Paper" ,1:"Scissor"}
you=youdict[youstr]

print(f"You choose {reversedict[you]}")
print(f"Computer chooses {reversedict[computer]}")

if(computer==you):
    print("Draw")
else:
    if(computer==-1 and you==0):
        print("You win")
    elif(computer==-1 and you==1):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You lose")
    elif(computer==0 and you==1):
        print("You win")
    elif(computer==1 and you==-1):
        print("You win")
    elif(computer==1 and you==0):
        print("You lose")
    else:
        print("Wrong Choice")
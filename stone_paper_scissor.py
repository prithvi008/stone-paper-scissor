import random

computer=random.choice([1,2,3])

idect={"stone":1,
       "paper":2,
       "scissor":3}
revidect={1:"stone",
       2:"paper",
       3:"scissor"}
ip=input("enter your choice: ")
user=idect[ip]

print("you choose: ",ip)
print("computer choose: ",revidect[computer])

if computer==user:
    print("draw")
else:
    if computer==1 and user==2:
        print("you win")
    elif computer==1 and user==3:
        print("you loss")
    elif computer==2 and user==1:
        print("you loss")
    elif computer==2 and user==3:
        print("you win")
    elif computer==3 and user==1:
        print("you win")   
    elif computer==3 and user==2:
        print("you loss")  
    else:
        print("something went wrong")       
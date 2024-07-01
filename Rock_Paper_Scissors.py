import random
import time


g_choices={"R":"Rock","P":"Paper","S":"Scissors"}
g_list=list(g_choices.keys())

while True:
    user=(input("User's throw: \nR for Rock \nP for Paper \nS for Scissors\n\nuser's turn: ")).upper()
    if user in g_list:
        print(f"User chose {g_choices[user]}")
        comp=random.choice(g_list)
        print()
        comp=random.choice(g_list)
        print()
        print("Now it's computer's turn",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(f"Computer chose {g_choices[comp]}")
        print()
        if user!=comp:
            if (user<comp and (comp!="S" and user!="P")) or (user=="S" and comp=="P"):
                print("User Wins!")
            else:
                print("Computer Wins!")
        else:
            print("It's a Draw!")
    else:
        print("Enter a Valid Choice")
        continue
    while True:
        select=input("Do you Wanna Play again?\nY/N: ").upper()
        print()
        if select=="N":
            f=1
            break
        elif select!="Y":
            print("Select a valid option")
            continue
        else:
            f=0
            break
    if f==1:
        break
    else:
        continue
    
            


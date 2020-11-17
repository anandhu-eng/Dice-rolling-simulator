#Dice rolling simulator
import random

def dice(number):
    if (number==1):
        print(".----------.")
        print("{          }")
        print("{     0    }")
        print("{          }")
        print(".----------.")
    if (number==2):
        print(".----------.")
        print("{          }")
        print("{  0   0   }")
        print("{          }")
        print(".----------.")
    if (number==3):
        print(".----------.")
        print("{          }")
        print("{ 0  0  0  }")
        print("{          }")
        print(".----------.")
    if (number==4):
        print(".----------.")
        print("{ 0      0 }")
        print("{          }")
        print("{ 0      0 }")
        print(".----------.")
    if (number==5):
        print(".----------.")
        print("{ 0      0 }")
        print("{     0    }")
        print("{ 0      0 }")
        print(".----------.")
    if (number==6):
        print(".----------.")
        print("{ 0  0  0  }")
        print("{          }")
        print("{ 0  0  0  }")
        print(".----------.")                

#creating a random loop
user_input=input("Press enter to roll or Q to exit")
while (user_input!='Q'):
    rand_num=random.randint(1,6)     #includes both 1 and 6
    dice(rand_num)
    user_input=input("Press enter to roll or Q to exit")


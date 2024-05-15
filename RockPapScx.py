import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list =[rock,Paper,Scissors]

print("chose '0' for ROCK \nchose '1' for PAPER \nchose '2' for SCISSOR ")
x=int(input("Enter your choice : "))

if x>3 or x<0:
    print("invalid number")
else:
     if x == 0:
        print(list[0])
     elif x == 1:
        print(list[1])
     else :
        print(list[2])
     comp_chose = random.randint(0, 2)
     print(f"Computer choices : {list[comp_chose]}")
     if comp_chose==x:
        print("It's a draw ")
     elif comp_chose==0 and x==2:
          print("You Lose")
     elif x==0 and comp_chose==2:
          # print(f"Computer choices : {comp_chose}")
          print("You Win🥳")
     elif comp_chose > x:
           #print(f"Computer choices : {comp_chose}")
          print("You Lose")
     elif x > comp_chose:
          # print(f"Computer choices : {comp_chose}")
          print("You Win🥳")


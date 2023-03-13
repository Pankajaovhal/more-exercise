# from random import randint

# def win():
#     print ('You win!')

# def lose():
#     print ('You lose!')

# while True:
#     player_choice = input('What do you pick? (rock, paper, scissors)')
#     player_choice.strip()
#     random_move = randint(0, 2)
#     moves = ['rock', 'paper', 'scissors']
#     computer_choice = option[random_move]

#     if player_choice ==computer_choice:
#         print ('Draw!')
#     elif 'rock' and coMp == 'scissors':
#         win()
#     elif  'paper' and comp == 'scissors':
#         lose()
#     elif play == 'scissors' and comp == 'paper':
#         win()
#     elif player == 'scissors' and Comp == 'rock':
#         lose()
#     elif payer == 'paper' and computer == 'rock':
#         win()
#     elif player == "rock" and comp == "paper":
#         lose()
#     aGain = input('Do you want to play again? (y or n)').strip()
#     if again == 'n':
#         break


import random

def win():
    print("you win.")
def lose():
    print("you lose.")
# def fun(pl_c,r_m,mo,c_c):
    # while False:
while True:
    pl_c=input("what do you pick?(rock,paper,scissors):")
    # pl_c.strip()
    # r_m=random.choice(mo)
    mo=["rock","paper","scissors"]
    c_c=random.choice(mo)
    if pl_c==c_c:
        print("draw")
    elif pl_c=="rock" and c_c=="scissors":
        win()
    elif pl_c=="paper" and c_c=="scissors":
        lose()
    elif pl_c=="scissors" and c_c=="paper":
        win()
    elif pl_c=="scissors" and c_c=="rock":
        lose()
    elif pl_c=="paper" and c_c=="rock":
        win()
    elif pl_c=="rock" and c_c=="paper":
        lose()
    again=input("do you want to play again?(y or n):").strip()
    if again=="n":
        break
# pl_c=input("what do you pick?(rock,paper,scissors)")
# pl_c.strip()
# r_m=random.choice(0,2)
# mo=["rock","paper","scissors"]
# c_c=[r_m]
# fun(pl_c,r_m,mo,c_c)


# import random

# def play():
#     u=input("what do you pick?(rock,paper,scissor):")
#     u=u.lower
#     c=random.choice(["rock","paper","scissors"])
#     if u==c:
#         return "it's a tie"
#     if is_win(u,c):
#         return "you win!"
#     return "you lose."



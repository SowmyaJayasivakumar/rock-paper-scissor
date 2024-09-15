import random

def user_win(user,comp,user_point, comp_point):
    if (user == 'r' and comp =='s') or (user == 's' and comp =='p') or (user == 'p' and comp =='r'):
        print(f"ur choice: {user}, comp choice: {comp}")
        user_point += 1
    else:
        print(f"ur choice: {user}, comp choice: {comp}")
        comp_point +=1
    return user_point,comp_point

user_point =0
comp_point = 0
while user_point<3 and comp_point <3:
        
    opt = ['r', 'p' , 's']
    comp = random.choice(opt)

    user = input("What do u choose ..  Rock(r) ,Paper(p) or Scissor.(s).? ").lower()

    # user wining condition
    if comp == user:
        print("Its a tie!")
    else:
        # Update points
        user_point, comp_point = user_win(user, comp, user_point, comp_point)
        
    print(f"Curent Points- U: {user_point} , Computer: {comp_point}")

if user_point==3:
    print("You win")
else:
    print("You Lose")
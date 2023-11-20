import random
# create matrix 3x3 as battle field
x = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
# combination whiches can bring Victory
win_positions = [
                (1,2,3,),
                (4,5,6,),
                (7,8,9,),
                (1,5,9,),
                (3,5,7,),
                (1,4,7,),
                (2,5,8,),
                (3,6,9,),
                 ]

# some additional vars
all_steps = [1,2,3,4,5,6,7,8,9]
computer_steps_history = []
person_steps_hystory = []
cross_or_zero = ['0', 'X']
status = False

person_sign = random.choice(cross_or_zero) # choise for signs
cross_or_zero.remove(person_sign)
computer_sign = cross_or_zero[0]

def computer_step():
    step = random.choice(all_steps)
    computer_steps_history.append(step)
    all_steps.remove(step)
    return step

# func for human steps, choose a step, save it to history, delete from all steps list 
def person_step():
    step = int(input("Ваш ход! "))
    if step in all_steps:
        person_steps_hystory.append(step)
        all_steps.remove(step)
        return step
    else:
        step = int(input("Выберете другой ход! "))

# check if there is winning combination
def check_status(lst):
    for steps in win_positions:
        if set(steps).issubset(lst):
            return True
# just for printing matrix
def print_matrix():        
    for i in x:
        print(*i)
    print('#'* 90)

# this func for changing diigit to player's
def change_sign(sign, step):
    for i in range(len(x)):
        if step in x[i]:
            x[i][x[i].index(step)] = sign
            break
# main func for game
def game_processing():
    print_matrix()
    global status   
    while status != True:
        change_sign(person_sign,person_step())
        status = check_status(person_steps_hystory)
        print_matrix()
        if status == True:
            winner = person
            break
        else:
            change_sign(computer_sign,computer_step())
            check_status(computer_steps_history)
            print_matrix()
            if status == True:
                winner = "Computer"
                break
    return winner
person = input("Let's start game, What's your name ")
print("The Winner is ", game_processing())
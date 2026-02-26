import tkinter as tk
import random

#studients names
enter_the_studients_name = str(input('enter the studint name: '))
R = enter_the_studients_name.split()
if len(R) != 5:
    print('the studients name is not 5')
else:
    n1 = R[0]
    n2 = R[1]
    n3 = R[2]
    n4 = R[3]
    n5 = R[4]
#fuctions of checking about scamming
def win():
    if n1 not in [n2, n3, n4, n5]:
        print('the names is correct')
    else:
        print(' the studient names arent correct')
        return enter_the_studients_name

random.choice (R)
winner = random.choice (R)
print('the winner is:', winner)
R.remove(winner)
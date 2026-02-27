import tkinter as tk
import random

#studients names
enter_the_studients_name = str(input('enter the studint name: '))
days = str(input('enter the days: '))
classes = int(input('enter the number of classes: '))

s = days.split()
R = enter_the_studients_name.split()

len(s)
x1 = s[0]
x2 = s[1]
x3 = s[2]
x4 = s[3]
x5 = s[4]

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
random.choice(s)
winner = random.choice (R)
marking = random.choice(s)
print('the winner is:', winner, 'the class is:', marking)

from random import random


def rock_paper_scissors( x, a=0.33333, b=0.66667):
    if( x < a):
        return 'R'
    elif( x < b):
        return 'P'    
    return 'S'

def cmp_rock_paper_scissors( a, b):
    if( a==b ):
        return 0
    if( a=='R' and b=='S'):
        return 1
    if( a=='P' and b=='R'):
        return 1
    if( a=='S' and b=='P'):
        return 1
    return -1


result = {}
result[-1] = 0
result[0] = 0
result[1] = 0

for i in range(0, 9999):
    #print('{0:2d}'.format(i))
    hand_a = rock_paper_scissors(random(), 0.25, 0.50)
    hand_b = rock_paper_scissors(random(), 0.5, 0.75)

    r = cmp_rock_paper_scissors( hand_a, hand_b)
    result[r] += 1

print('{}'.format(result))


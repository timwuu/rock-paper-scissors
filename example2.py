#
#   initial probability distribution (R,P,S) = (1.0/3.0, 1.0/3.0, 1.0/3.0)
#   player B: change the probability distribution after each hand
#        if previous hand is Rock,    then (R,P,S) = (0.25, 0.25, 0.50)
#        if previous hand is Paper,   then (R,P,S) = (0.50, 0.25, 0.25)
#        if previous hand is Scissor, then (R,P,S) = (0.25, 0.50, 0.25)
#
#   2017.11.08 timijk: player A learn policy from experience
#

from random import random

PROBIBILITY_ROCK = 1.0/3.0
PROBIBILITY_PAPER = 1.0/3.0

#learning rate
ALPHA = 0.02


def rock_paper_scissors( a=PROBIBILITY_ROCK, b=PROBIBILITY_PAPER):
    x = random()
    if x < a:
        return 'R'
    elif x < a + b:
        return 'P'
    return 'S'

def rock_paper_scissors_2( x=None):
    if x == None:
        return rock_paper_scissors()

    if x == 'R':
        return rock_paper_scissors(0.25, 0.25)  # Rock -> Scissor
    if x == 'P':
        return rock_paper_scissors(0.5, 0.25)  # Paper -> Rock
    if x == 'S':
        return rock_paper_scissors(0.25, 0.5)  # Scissor -> Paper

def cmp_rock_paper_scissors( a, b):
    if a == b:
        return 0
    if a == 'R' and b == 'S':
        return 1
    if a == 'P' and b == 'R':
        return 1
    if a == 'S' and b == 'P':
        return 1
    return -1

def hand2index( hand):
    if hand == 'R':
        return 0
    elif hand == 'P':
        return 1
    else:
        return 2

def learn( prob_matrix, prv_hand_x, hand_y, result):

    if prv_hand_x == None:
        return

    i = hand2index(prv_hand_x)
    j = hand2index(hand_y)
    
    if result == 1: # win
        j_w = j
    elif result == 0:  # draw
        j_w = (j+1)%3
    else: # lose
        j_w = (j+2)%3

    #print('{}.{}'.format(i,j))
    
    j_l = (j_w+1)%3
    j_d = (j_w+2)%3


    prob_w = min( prob_matrix[i][j_w] + ALPHA, 1.0)
    prob_l = max( prob_matrix[i][j_l] - ALPHA/2.0, 0.0)
    prob_d = max( prob_matrix[i][j_d] - ALPHA/2.0, 0.0)

    # normalize    

    _sum = prob_w + prob_l + prob_d

    prob_matrix[i][j_w] = prob_w / _sum
    prob_matrix[i][j_l] = prob_l / _sum
    prob_matrix[i][j_d] = prob_d / _sum

    return

result = {}
result[-1] = 0
result[0] = 0
result[1] = 0

player_a = [[ 1.0/3.0 for x in range(3)] for y in range(3)]

print( player_a[0])
print( player_a[1])
print( player_a[2])

hand_b = None

prob_rock = 1.0/3.0
prob_paper = 1.0/3.0

for i in range(0, 9999):
    #print('{0:2d}'.format(i))
    prv_hand_b = hand_b
    hand_a = rock_paper_scissors( prob_rock, prob_paper)
    hand_b = rock_paper_scissors_2( prv_hand_b)

    r = cmp_rock_paper_scissors( hand_a, hand_b)
    result[r] += 1

    #print('{} {} :{}'.format( hand_a, hand_b, r))

    learn( player_a, prv_hand_b, hand_a, r)

    # player_a set the probability of the next hand
    i = hand2index(hand_b)
    prob_rock = player_a[i][0]
    prob_paper = player_a[i][1]

print('{}'.format(result))

print( player_a[0])
print( player_a[1])
print( player_a[2])


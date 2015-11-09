import sys
from math import floor, ceil
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

 # w: width of the building.
 # h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input()) # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]

def dreiviertel(Min, Max):
    return (Min + Max) / 2
# game loop

xMAX = w - 1
yMAX = h - 1
xMIN = 0
yMIN = 0


while 1:
    bomb_dir = raw_input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # the location of the next window Batman should jump to.

    if bomb_dir == "U":
        yMAX = y0 - 1
        
    elif bomb_dir == "D":
        yMIN = y0 + 1
        
    elif bomb_dir == "L":
        xMAX = x0 - 1
    
    elif bomb_dir == "R":
        xMIN = x0 + 1

    elif bomb_dir == "UR": 
        xMIN = x0 + 1
        yMAX = y0 - 1 

    elif bomb_dir == "UL":
        xMAX = x0 - 1
        yMAX = y0 - 1
        
    elif bomb_dir == "DR":
        xMIN = x0 + 1
        yMIN = y0 + 1
    elif bomb_dir == "DL":
        xMAX = x0 - 1
        yMIN = y0 + 1

        
    x0 = dreiviertel(xMIN, xMAX)
    y0 = dreiviertel(yMIN, yMAX)
    
    print int(x0), int(y0)

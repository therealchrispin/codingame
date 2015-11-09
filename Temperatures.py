import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input()) # the number of temperatures to analyse
temps = raw_input() # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages...33


liste1 = temps.split(" ")
liste = []

if len(temps) == 0:
    print "0"
else:
    for i in range(len(liste1)):
        x = int(liste1[i])
        liste.append(x)
    if min(liste, key=abs) < 0 and min(liste, key=abs)*-1 in liste:
        print(min(liste, key=abs)*-1)
    else:
        print(min(liste, key=abs))

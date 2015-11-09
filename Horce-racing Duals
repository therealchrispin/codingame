import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
list = []
n = int(raw_input())
for i in xrange(n):
    pi = int(raw_input())
    list.append(pi)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
  
list.sort()
i = 0 
liste = []
while i < len(list)-1:
    b = list[i+1] - list[i]
    liste.append(b)
    i += 1

print(min(liste, key=abs))

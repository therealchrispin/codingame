import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
vs = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."


li = vs.split()
nli = []
difl = 0
def test(nli,difl):
    mini = min(nli)
    if mini == nli[0]:
        maxi = 0
    else:
        maxi = max(nli[:nli.index(min(nli))]) 
    erg = maxi - mini 
    if erg > difl:
        difl = erg
    if len(nli[nli.index(min(nli)):]) > 1:
        nli = nli[nli.index(min(nli))+1:]
        test(nli, difl)
    else:
        print(difl*-1)
    
    
if len(li) > 0:
    for i in range(len(li)):
        nli.append(int(li[i]))
    test(nli, difl)
else:
    print(0)
    

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
liste1 = []

l, h = [int(i) for i in raw_input().split()]
for i in xrange(h):
    numeral = [raw_input()]
    liste1.append(numeral)

num1liste = []    
num1 = ""
s1 = int(raw_input())
for i in xrange(s1):
    num_1line = raw_input()
    num1 += num_1line

num1liste.append(num1)    
    
num2liste = []    
num2 = ""    
s2 = int(raw_input())
for i in xrange(s2):
    num_2line = raw_input()
    num2 += num_2line
    
num2liste.append(num2)
    
operation = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def translate(stri,liste,nliste,l):
    for i in range(len(stri)/l):
        if liste.index(stri) == 0:
            nliste.append(stri[(i)*l:((i)*l)+l])
        else: 
            nliste[i] += stri[(i)*l:((i)*l)+l]
            
def einezahl(numliste):
    ueliste = []
    for i in numliste:
        translate(i,numliste,ueliste,l*h)
    teiln = " ".join(ueliste).split()
    neueliste = []
    for i in teiln:
        if i in dicti:
            neueliste.append(dicti[i])
    return neueliste
    
def vigesiDezi(stellenwerte):
    if len(stellenwerte) > 0:
        stellenwerte.reverse()
        for i in range(len(stellenwerte)):
            stellenwerte[i] = int(stellenwerte[i])*(20**i)
    return sum(stellenwerte)

def DeziVigesi(zahl,liste):
    n = zahl/20
    if zahl == 20:
        liste.append(zahl/20)
    else:
        liste.append(zahl%20)
        
    if zahl/20 == 0  and zahl&20 == 0:
        return liste.reverse()
    else:
        DeziVigesi(n,liste)
#------------------------------------------------------------------#
liste = []
a = 0
for i in liste1:
    line = liste1[a][0]
    a+=1
    liste.append(line)
    

nli = []

for stri in liste:
    translate(stri,liste,nli,l)

dicti = {}
for m in nli:
    dicti[m] = nli.index(m)

#--------------------------------------------------------------------#
nummer1 = vigesiDezi(einezahl(num1liste))
nummer2 = vigesiDezi(einezahl(num2liste))

if operation == "+":
    nummer3 = nummer1 + nummer2
elif operation == "*":
    nummer3 = nummer1 * nummer2
elif operation == "/":
    nummer3 = nummer1 / nummer2
elif operation == "-":
    nummer3 = nummer1 - nummer2

#---------------------------------------------------------------------#


ergebnis = []
DeziVigesi(nummer3,ergebnis)


if ergebnis[0] == 0 and len(ergebnis) > 1:
    ergebnis.remove(0)

for ai in ergebnis:
    for key, value in dicti.iteritems():
        if ai == value:
            for i in range(len(key)/l):
                print key[(i)*l:((i)*l)+l]





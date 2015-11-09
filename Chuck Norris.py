import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = raw_input()
message.strip()
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

chn=""
for ch in message:
    if len(bin(ord(ch))[2:]) < 7:
        chn += "0" + bin(ord(ch))[2:]
    else:
        chn += bin(ord(ch))[2:]

i = 0
chn1 = list(chn)
while i < len(chn1)-1:
    if chn1[i] != chn1[i+1]: 
        chn1.insert(i+1, " ")
        i +=2
    else:
        i +=1
        
cn = "".join(chn1).split()
y = 0
while y < len(cn):
    if "1" in cn[y]:
        cn[y] = "0 "+ cn[y].replace("1","0")
        y +=1
    elif "0" in cn[y]:
        cn[y] = "00 "+ cn[y] 
        y +=1
    else:
        y+=1

print(" ".join(cn))

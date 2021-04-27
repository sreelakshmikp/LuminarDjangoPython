import re
valid=[]
rule="[K][L][0-9]{2}[a-zA-Z]{2}[0-9]{4}"
f=open("validvechile","r")
for numbers in f:
    number=numbers.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        valid.append(number)
print(valid)
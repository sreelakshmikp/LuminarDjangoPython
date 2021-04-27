import re
rule="[\w.]+[@][g][m][a][i][l][.][c][o][m]"
var_name=input("enter mail id")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid mail id")
else:
    print("valid mail id")
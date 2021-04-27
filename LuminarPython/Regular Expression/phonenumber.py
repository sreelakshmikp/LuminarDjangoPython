import re
rule="\d{10}"
var_name=input("enter variable name")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid number")
else:
    print("valid number")
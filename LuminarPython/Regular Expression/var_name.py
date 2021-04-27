import re
rule="[a-k][369][a-zA-Z]*"
var_name=input("enter variable name")
matcher=re.fullmatch(rule,var_name)
if matcher==None:
    print("invalid variable")
else:
    print("valid variable name")
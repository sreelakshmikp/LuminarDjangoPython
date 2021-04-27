import re
# pattern="a+"
# pattern="a*"
# pattern='a{2}'
# pattern='a{2,3}'  --->minimum 2 and maximum 3
matcher=re.finditer(pattern,"aaaaaaabbbaaaabbbabaab")
for match in matcher:
    print(match.start())
    print(match.group())
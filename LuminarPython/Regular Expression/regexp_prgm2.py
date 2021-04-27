# either a b or c
import re
# pattern='[abc]'
# pattern='[a-z]'
# pattern='[A-Z]'
# pattern='[a-zA-Z]'
# pattern='[0-9]'
# pattern='[a-zA-Z0-9]'
# pattern='[^a-zA-Z0-9]'

# predefined characters
# pattern='[\s]' --->space
# pattern='[\d]' --->digits
# pattern="\D" --->[^0-9]
# pattern="\w" --->[a-zA-Z0-9]
# pattern="\W"  --->special characters
matcher=re.finditer(pattern,"abc _Z7K@")
for match in matcher:
    print(match.start())
    print(match.group())
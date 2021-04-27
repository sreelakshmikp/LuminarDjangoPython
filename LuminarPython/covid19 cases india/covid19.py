f=open("dataset","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmed_case=data[-1]
    for word in data:
        if word not in dict:
            dict[word]=confirmed_case
        else:
            dict[word]=confirmed_case
    print(state,",",confirmed_case)
maxword=max(dict,key=confirmed_case.get)
print(maxword)
minword=min(dict,key=confirmed_case.get)
print(minword)
# word count
text="hello hai how hai hello hai"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
data=sorted(dict,key=dict.get,reverse=True)
print(data)
maxword=max(dict,key=dict.get)
print(maxword)
minword=min(dict,key=dict.get)
print(minword)
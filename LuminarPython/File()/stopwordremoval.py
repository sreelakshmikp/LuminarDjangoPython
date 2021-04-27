f=open("demo2","r")
dict={}
stopwords=["is","are"]
for lines in f:
    words = lines.rstrip("\n").split(" ")
    for word in words:
        if word in stopwords:
            pass
        else:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
print(dict)
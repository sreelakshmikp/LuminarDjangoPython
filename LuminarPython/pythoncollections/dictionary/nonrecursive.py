pattern="AABBCD"
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
print(dict)
for k,v in dict.items():
    # print(k,v)
     if v==1:
        print(k)
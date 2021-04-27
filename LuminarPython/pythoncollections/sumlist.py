lst=[3, 4, 6, 7, 8]
elist=list()
olist=[]
# for num in lst:
#     if num>5:
#         print(num+1)
#     else:
#         print(num-1)

for i in lst:
    if i%2==0:
        elist.append(i)
    else:
        olist.append(i)
print(elist)
print(elist)
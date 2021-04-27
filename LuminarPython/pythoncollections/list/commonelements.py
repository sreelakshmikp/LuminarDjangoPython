lst1=[1,2,3,5,4]
lst2=[1,2,6,7,8,4]
lst1.sort()
lst2.sort()
i=0
j=0
for i in lst1:
    for j in lst2:
        if i==j:
            print(i)
        elif i>j:
            j+=1
        elif i<j:
            i+=1
print()

# another method low complexity
lst1=[1,2,3,5,4]
lst2=[1,2,6,7,8,4]
lst1.sort()
lst2.sort()
pos1=0
pos2=0
while(pos1<len(lst1)) & (pos2<len(lst2)):
    if(lst1[pos1]==lst2[pos2]):
        pos1+=1
        pos2+=1
        print(lst1[pos1])
    elif(lst1[pos1]>lst2[pos2]):
        pos2+=1
    elif(lst1[pos1]<lst2[pos2]):
        pos1+=1
    print()
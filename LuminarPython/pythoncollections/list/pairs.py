# lst=[1,2,3,4]
# num=int(input("enter number"))
# flag=0
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==num:
#             print(lst[i],",",lst[j])
#             flag=1
#             break
# if flag==0:
#     print("no pairs")

# low complexity program
lst=[1,2,3,4]
num=int(input("enter number"))
low=0
upp=len(lst)-1
for i in range(0,len(lst)):
    sum=lst[low]+lst[upp]
    if(sum==num):
        print("pairs",lst[low],lst[upp])
        low+=1
    elif(sum<num):
        low+=1
    else:
        upp-=1
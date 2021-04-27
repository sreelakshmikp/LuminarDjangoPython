arr=[3, 4, 2, 1, 8, 7, 6]
arr.sort()
element=int(input("enter element"))
flag=0
low=0
up=len(arr)-1
while(low<=up):
    mid=(low+up)//2
    if(element>arr[mid]):
        low=mid+1
    elif(element<arr[mid]):
        up=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")
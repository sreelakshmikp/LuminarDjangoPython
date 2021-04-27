lst=[1,2,3,4]
op=[num**2 for num in lst]
print(op)

# find even numbers from list
evens=[num for num in lst if num%2==0]
print(evens)

# common elements from 2 list
lst1=[1,2,3]
lst2=[2,3,4]
common=[num1 for num1 in lst1 for num2 in lst2 if num1==num2]
print(common)

# pairs from two list
pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
print(pairs)

# print list from nested list as [10,20,30,40,50,60]
list=[[10,20],[30,40],[50,60]]
new_lst=[num for lst in list for num in lst]
print(new_lst)

list1=[4,3,2,5,6,7,9,8]
new=[num+1 if num>5 else num-1 if num<5 else 5 for num in list1]
print(new)
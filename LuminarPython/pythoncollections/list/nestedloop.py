# for i in range(1,5):
#     for j in range(1,5):
#         print(j,end="")
#     print()

# pattern using nested loop
# for i in range(1,5):
#     print(str(i)*i)

# for row in range(1,5):
#     for col in range(1,(row+1)):
#         print(col,end="")
#     print()

# print star in triangle shape
for i in range(1,6):
    for j in range(1,10):
        if (i==5)|(i+j==6)|(j-i==4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
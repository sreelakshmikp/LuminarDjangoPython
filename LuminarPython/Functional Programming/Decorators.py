def sub(num1,num2):
    return num1-num2
print(sub(10,20))

# always substract highest from lowest--->we can do swapping
def sub(num1,num2):
    if num1<num2:
        num1,num2=num2,num1
    return num1-num2
print(sub(10,20))
# but here we are changing the function

# DECORATORS

# here a new function is creating ie, adding a new feature without changing the main function
def sub_smart(fun):#fun=div
    def inner(num1,num2):#10,20
        if num1<num2:#10<20
            num1,num2=num2,num1
        return fun(num1,num2)
    return inner
@sub_smart
def sub(num1,num2):
    return num1-num2
print(sub(10,20))
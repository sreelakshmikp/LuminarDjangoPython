no1=int(input("enter num1"))
no2=int(input("enter num2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)
print("database transaction")
print("file operation")
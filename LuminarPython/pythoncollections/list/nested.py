employees=[
    [100,"akhil","developer",2,50000,1989,1995],
    [101,"anu","developer",3,60000,1970,1990],
    [102,"james","qa",1,35000,1989,1991],
    [103,"sree","ba",1,4500,1998,1999],
]
for emp in employees:
    print(emp[1])
for salary in employees:
    print(salary[4])
for dev in employees:
    print(dev[2])
# print details of developer
for emp in employees:
    if emp[2]=="developer":
        print(dev)
# print sum of salary
total=0
for emp in employees:
    total+=emp[4]
print(total)
# print highest salary
sallist=[]
for emp in employees:
    sallist.append(emp[4])
print(max(sallist))

# print employees worked in 90's
for emp in employees:
    if emp[5]>=1990 & emp[6]<=2000:
        print(emp)
# high exp employee details
exp=[]
for emp in employees:
    emp.append(emp[3]-emp[2])
high=max(emp)
for emp in employees:
    exp=emp[3]-emp[2]
if(high==exp):
    print(emp)
# print details of developers
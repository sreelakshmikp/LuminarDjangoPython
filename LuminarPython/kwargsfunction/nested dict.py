students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"gokul","course":"django","qualification":"mca"},
    1002:{"id":1002,"name":"nikhil","course":"django","qualification":"btech"}
}
# print(students[1000]["name"])


# id=int(input("enter student id"))
# if id in students:
#     print(students[id]["name"])
# else:
#     print("invalid")

id=int(input("enter student id"))
property=input("enter student property") #course
if id in students:
    print(students[id]["name"])
    if property in students[id]:
        print(students[id][property])
    else:
         print("invalid property")
else:
    print("invalid id")


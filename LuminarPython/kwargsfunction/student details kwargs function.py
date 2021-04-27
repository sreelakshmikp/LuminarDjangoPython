students={
    1000:{"id":1000,"name":"akhil","course":"django","qualification":"btech"},
    1001:{"id":1001,"name":"gokul","course":"django","qualification":"mca"},
    1002:{"id":1002,"name":"nikhil","course":"django","qualification":"btech"}
}
# def get_student(id):
#     if id in students:
#         print(students[id]["name"])
# get_student(1002)


def get_students(**kwargs):
    id=kwargs["id"]
    prop=kwargs["property"]
    if id in students:
        print(students[id]["name"])
        if prop in students[id]:
            print(students[id][prop])
        else:
            print("invalid property")
    else:
        print("student doesnot exist with given id")
get_students(id=1001,property="course")
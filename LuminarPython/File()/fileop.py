f=open("demo","r")
list=[]
for lines in f:
    list.append(lines.rstrip("\n"))
print(list)

# remove duplicate
f=open("demo","r")
st=set()
for lines in f:
    st.add(lines.rstrip("\n"))
print(st)
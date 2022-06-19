user_string= input("enter a string")
w = user_string.split()
d = {}
for i in w:
    if i not in d.keys():
        d[i]=0
    d[i]= d[i]+1
print (d)

string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
l=[]
i=0
while i<len(string_list):
    if string_list[i] not in l:
        l.append(string_list[i])
    i+=1
print(l)
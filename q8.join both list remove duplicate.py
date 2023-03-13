list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8,8,2]
l=[]
i=0
while i<len(list1):
    list1.append(list2)
    if list1[i] not in l:
        l.append(list1[i])
    i+=1
print(l)
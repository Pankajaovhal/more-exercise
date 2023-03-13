list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
l=[]
i=0
while i<len(list2):
    if list2[i] in list1:
        l.append(list2[i])
    i+=1
print(l)
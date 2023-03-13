def mx_marks(marks):
    i=0
    mx=0
    while i <len(marks):
        if type(marks[i])==list:
            j=0
            while j<len(marks[i]):
                if marks[i][j]>mx:
                    mx=marks[i][j]
                j+=1
            print(mx)
        i+=1
marks = [[45, 21, 42, 63], [12, 42, 42, 63], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
mx_marks(marks)
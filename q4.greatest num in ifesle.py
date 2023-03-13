m=int(input("enter number:"))
m1=int(input("enter number:"))
m2=int(input("enter number:"))
if m>m1 and m>m2:
    print(m,"is greatest.")
elif m1>m and m1>m2:
    print(m1,"is greatest.")
elif m2>m and m>m1:
    print(m2,"is greatest.")
else:
    print("none")
def hn(n):
    sum=0
    z=n
    d=n%10
    sum=sum+d
    n=n/10
    if z%sum==0:
        return("true")
    else:
        return("false")     
n=int(input("enter number:"))
print(hn(n))

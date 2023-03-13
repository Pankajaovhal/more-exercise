n=input("enter your password:")
if len(n)>=6 and len(n)<=16:
    if "$" in n:
        if "2" or "8" in n:
            if "A" or "Z" in n:
                print("your password is stronge.")
            else:
                print("your password is not stronge.")
        else:
            print("your password is not stronge.")
    else:
        print("your password is not stronge.")
else:
    print("your password is not stronge.")
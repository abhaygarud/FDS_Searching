def fib():
    n=int(input("enter the number for fibonnic"))
    a=0
    b=1
    if n==1:
        print(a)
    elif n<=-999:
        print("invalid input")
    else:
        print(a)
        print(b)
        for i in range (2,n):
        
            c=a+b
            a=b
            b=c
            if c>=100:
                break
            print(c)
fib()
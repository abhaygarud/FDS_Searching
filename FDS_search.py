pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
               u= mid-1
    return False

def fibonic(x):
        if x<1:
            return 0
        if x==1:
            return 1
        else:
            return fibonic(x-1)+fibonic(x-2)
    
#fibonic=[1,1,2,3,5,8,13,21,]
def fib_search(list,n):
    m=0
    while fibonic(m)<len(list):
        m+=1
        ofset=-1
    while fibonic(m)>1:  
        i=min(ofset+fibonic(m-2),len(list)-1)
        if(n>list[i]):
            m=m-1
            ofset=i
        elif (n<list[i]):
            m=m-2
        else:
            return i

print(fib_search(list,n))




list=[1,2,3,4,5,6,7,8,9,10]
print(list)
n=int(input("enter the student you want to check he was present or absent :"))
print(fib_search(list,n))

if search(list,n):
    print(n," number of student was presnet and he was at the position:",pos)
else:
    print("student was absnet")
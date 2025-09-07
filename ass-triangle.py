n1=int(input("Enter first side:"))
n2=int(input("Enter second side:"))
n3=int(input("Enter third side:"))
flag=1
l=[n1,n2,n3]
l=sorted(l)
#checking whether forms a triangle or not
if n1+n2>n3 and n2+n3>n1 and n3+n1>n2:
    print("The given sides form a triangle")
else:
    flag=2
    print("the given sides wont form a triangle:")
if flag==1:
    if n1==n2==n3:
        print("forming equilateral triangle")
    elif n1==n2 or n2==n3 or n3==n1:
        print("forming Isosceles triangle")
    elif n1!=n2 and n2!=n3 and n3!=n1:
        print("Forming scalen triangle")
    if (l[-1])**2 == (l[0])**2 + (l[1])**2:
        print("formes rightangled triangle")



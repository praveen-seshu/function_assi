#Different ways of Finding Armstrong number using python

#1)	using string conversion in for loop
n=int(input("Enter a number:"))
l=len(str(n))
sum=0
for i in str(n):
    sum+=int(i)**l
if n==sum:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")

#2) using modulus in for loop
n=int(input("Enter a number:"))
nc=n
s=0
for i in range(len(str(n))):
    l=nc%10
    s+=l**len(str(n))
    nc=nc//10
if n==s:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not armstrong number")

#3)using while loop and modulus
n=int(input("Enter a number:"))
nc=n
s=0
while nc!=0:
    l=nc%10
    s+=l**len(str(n))
    nc=nc//10
if n==s:
    print(f"{n} is armstromg number")
else:
    print(f"{n} is not armstrong number")

#4) printing Armstrong numbers in a range
n=int(input("Enter a number:"))
s=0
for i in range(n+1):
    s=0
    for j in str(i):
        l=len(str(i))
        s=s+int(j)**l
    if i==s:
        print(i)

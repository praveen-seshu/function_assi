#add of two numbers
def add_n(a,b):
    return(a+b)
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
res=add_n(n1,n2)
print(res)

#square of number
def sqr(num):
    return (num**2)
n2=int(input("enter a number:"))
res=sqr(n2)
print(res)
#number even or odd
def ev_odd(num):
    return f'{num} is even' if num % 2==0 else f'{num} is odd'
n2=int(input("enter a number:"))
res=ev_odd(n2)
print(res)
#factorial of a number
def factorial(num):
    i=num
    fact=1
    while i >0:
        fact*=i
        i-=1
    return f'factorial is {fact}'
n2=int(input("enter a number:"))
res=factorial(n2)
print(res)
#great of three numbers
def max_of_3(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return f" greater of three numbers is {n1}"
    elif n2 > n1 and n2 > n3:
        return f"great of three numbers is {n2}"
    else:
        return f'{n3} is greater'

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
res=max_of_3(n1,n2,n3)
print(res)
#cnt of ovels
def no_ovels(str1):
    str1=str1.lower()
    cnt=0
    for i in str1:
        if i in ['a','e','i','o','u']:
            cnt+=1
    return f"count of vowels is:{cnt}"
n1=input("Enter a string:")
res=no_ovels( n1)
print(res)

#sum of elements in a list
def sum_of_ele(lst):
    sum1=0
    for i in lst:
        sum1=sum1+i
    return (sum1)
lst=[]
for i in input("Enter space saperated values:").split(" "):
    if i.isdigit():
        lst.append(int(i))
res=sum_of_ele(lst)
print(res)

#reverse of string
def rev_str(str1):
    str2=[]
    for i in range(len(str1)-1,-1,-1):
        str2.append(str1[i])
    return "".join(str2)
str1=input("Enter a string:")
res=rev_str(str1)
print(res)

#pallindrom or not
def pallin(str1):
    str2=[]
    for i in range(len(str1)-1,-1,-1):
        str2.append(str1[i])
    str2= "".join(str2)
    if str1 == str2:
        return("it is pallindrom:")
    else:
        return ('not pallindrom')
string=input("Enter a string:")
res=pallin(string)
print(res)

#even numbers in a list
def even_print(lst1):
    lst2=[]
    for i in lst1:
        if i%2==0:
            lst2.append(i)
    return lst2
lst1=[]
for i in input("Enter ssv").split(" "):
    if i.isdigit():
        lst1.append(int(i))
print(lst1)
res=even_print(lst1)
print(res)


#area of circle
def area(r):
    return f'area of circle is:{3.14*r**2}'
radius=int(input("enter a number:"))
res=area(radius)
print(res)
#length of string
def len_str(str1):
    cnt=0
    for i in str1:
        cnt+=1
    return cnt
str1=input("Entre string:")
res=len_str(str1)
print(res)
#averge of any numbers
def avg(*a):
    sum1=sum(a)
    return sum1//2
res=avg(1,2,3,4,5,6)
print(res)






            







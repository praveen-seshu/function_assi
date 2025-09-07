n=int(input("enter a number:"))
str1=str(n)
l=[]
l2=[]
print("even numbers are:")
for i in str1:
    if int(i)%2==0:
        print(int(i),end=" ")
print()
print("prime numbers are:")
for i2 in str1:
    cnt=0
    for j in range(1,int(i2)):
        if int(i2)%j==0:
            cnt+=1
    if cnt==1:
        print(int(i2),end=" ")
print()
product=1
mat=[
    [1,2,3,4],
    [4,5,6,7],
    [3,5,7,8]
]
for row in mat:
    for num in row:
        product*=num
print(product)




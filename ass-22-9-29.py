#socks problm
list4=['red','red','red','green','green','green','pink','blue']
dict1={}
out_list=[]
day=0
for i in list4:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
for j,k in dict1.items():
    day+= k // 2
print("you can sustain ",day,'days')

#finding the missing numbers in the sequence
number = int(input("Enter a number:"))
n = number
sort_list = []
while n > 0 :
    sort_list.append (n % 10)
    n= n // 10
sort_list1 = sorted (sort_list)
print("The missing numbers are")
for i in range (min (sort_list1) , max(sort_list1)):
    if i not in sort_list1:
        print(i,end=' ')

#matrix addition using range
matrix=[
    [1,2,3,4],
    [5,6,7],
    [8,9,10]
]
Total_sum=0
for i in range(0,len(matrix)):
    row=matrix[i]
    for val in range(0,len(row)):
        Total_sum += row[val]
print(Total_sum)
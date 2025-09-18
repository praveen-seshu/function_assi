list5=[23,45,1,2,78,41,34,68,80]
cnt=0
for i in range(0,len(list5)-1):
    flag=True
    for j in range(0,len(list5)-1-i):
        if list5[j] > list5[j+1]:
            cnt+=1
            flag=False
            list5[j] , list5[j+1] = list5[j+1] , list5[j]
    if flag==True:
        break
search_ele=int(input("Enter element to search:"))
flag2=True
low , high = 0 , len(list5)//2 + 1
while low <= high:
    mid= (low+high)//2
    if list5[mid] == search_ele:
        flag=False
        print("element found at inded",mid)
        break
    elif mid > search_ele:
        high = mid - 1
    else:
        low = mid + 1 
if flag==True:
    print("Element not found")
print('sorted list is :',list5)
print('Number of swaps taken to sort is:',cnt)
# sorting in descending order
list2=[34,56,12,34,90]
for j in range(0,len(list2)-1):
    flag=True
    for i in range(0,len(list2)-1-j):
        if list2[i] < list2[i+1]:
            flag=False
            list2[i] , list2[i+1] = list2[i+1] , list2[i]
    if flag==True:
        break
print(list2)

#checking bubble sort for list with strings = sorting occures in dictionary order
list1=['praveen','seshu','ambati']
for j in range(0,len(list1)-1):
    flag=True
    for i in range(0,len(list1)-1-j):
        if list1[i] > list1[i+1]:
            flag=False
            list1[i] , list1[i+1] = list1[i+1] , list1[i]
    print(list1)
    if flag==True:
        break

#sorting list of string base on length
list3=['praveen','seshu','ambati']
for j in range(0,len(list3)-1):
    flag=True
    for i in range(0,len(list3)-1-j):
        if len(list3[i]) > len(list3[i+1]):
            flag=False
            list3[i] , list3[i+1] = list3[i+1] , list3[i]
    if flag==True:
        break
    print(list3)
    
#sorting nested list base on first index
list4=[[3,4,5,6],[7,8,4,25],[4,7,9,34,3],[1,3,4,6,7]]
for j in range(0,len(list4)-1):
    flag=True
    for i in range(0,len(list4)-1-j):
        ind1=list4[i]
        ind2=list4[i+1]
        if ind1[0] > ind2[0]:
            flag=False
            list4[i] , list4[i+1] = list4[i+1] , list4[i]
    if flag==True:
        break
print(list4)
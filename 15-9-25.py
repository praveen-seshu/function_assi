#reverse a stringby function
def reverse_str(str):
    new_str=[]
    for i in range(len(str1)-1,-1,-1):
        #print(s[i],end="")
        new_str.append(str1[i])
    new_str="".join(new_str)
    print(new_str)
reverse_str(input("Enter a string:"))
#sum of digits in the list 
def sum_Of_dig_in_lst(list1):
    sum_list=[]
    for i in list1:
        i=str(i)
        sum=0
        for j in i:
            sum+=int(j)
        sum_list.append(sum)
    print(sum_list)
sum_Of_dig_in_lst([23,123,1234,765])
#finding max digit in the given number
def max_dig_in_num(number):
    n=str(number)
    max_num=n[0]
    for i in n:
        if int(i) > int(max_num):
            max_num=int(i)
    print("max digit in the given number is :",max_num)
max_dig_in_num(9876543123456)
#finding max digit in list of numbers
def max_dig_in_lst_num(list1):
    max_list=[]
    for i in list1:
        i=str(i)
        max_dig=i[0]
        for j in i:
            if int(j) > int(max_dig):
                max_dig=int(j)
        max_list.append(int(max_dig))
    print(max_list)
max_dig_in_lst_num([23,123,12834,765])

#returning false if number in list contain duplicant digit else rerurn true out put in list 
list4=[1123,4432,7789,4458,6753,9086]
out_list=[]
for i in list4:
    second_list=[]
    i=str(i)
    for j in i:
        if int(j) not in second_list:
            second_list.append(int(j))
        else:
            out_list.append("false")
            break
    else:
        out_list.append("True")
print(out_list)
#sum of all elements in teh matrix
mart=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total_sum=0
for row in mart:
    for val in row:
        total_sum+= val
print(total_sum)
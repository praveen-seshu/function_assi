#inbuilt methods for list
# 1)append=will take only one argument(only one element) and adds the element in the end of the list
l1=[1,2,3,45]
l1.append(4)
l1.append([1,2,3,5])
print(l1)
#2)extend=can add multiple elements to an existing list with the help of any iterable(list,tuple,string,set,) and adds at the end
l2=[1,2,3,4,5]
l2.extend([5,6,7,8])
l2.extend((9,10))
# l2.extend((9))#error must be iterable one 
l2.extend({10,11})
l2.extend('ab')
print(l2)
#3)insert= takes two arguments index and element and adds in a spefic index
l3=[1,2,3,4]
l3.insert(2,10)
l3.insert(3,[1234])
print(l3)
#4)clear=it will empty teh list and returns none
l4=[1,2,3,4,5]
print(l4)
l4.clear()
print(l4)
#5)pop=used to remove elements from the list,when index specified remove specic index if not remove end element
l5=[1,2,3,4,5]
print(l5.pop())
print(l5.pop(0))
# print(l5.pop(100)) out of range error
#6)remove(ele)=remove the first occurance of the element
l6=[1,2,2,3,3,4,5,6]
l6.remove(2)
print(l6)
#7).count(ele) or .count used to count number of duplicant of an element
l7=[1,2,2,2,3,4,5,6]
print(l7.count(2))
#8).index(ele) used to find the index of the element just for the first occurance
l8=[1,2,2,3,4,5,6]
print(l8.index(2))
print(l8.index(2,0,4))
#9)reverse =used to print the the list of elements in the reversed order and changes the original list and returns none
ll9=[1,2,3,4,5]
print(ll9.reverse())#none
print(ll9)
#9.1)reversed()= it will reverse the list by keeping the original list unchanged,and return now list
lll9=[1,2,3,4,5,6]
print(reversed(lll9))#<list_reverseiterator object at 0x000001E236DBFF40>
print(list(reversed(lll9)))
print(lll9)
#9.2)using slicing operator
l9=[1,2,3,4,5,6,7]
print(l9[::-1])
for i in reversed(l9):
    print(i,end=" ")
print()
# inplace 10)sort=sort the list in ascending order and changes the original list
l10=[2,3,4,1,5,6]
print(l10.sort())#none
print(l10)
#normal sorting sorted(list)=wont change the original list returns the new list
ll10=[1,4,3,6,7]
list2=sorted(ll10)
print(list2)
print(ll10)
#sort in descending order
lll10=[1,5,3,7,4]
list3=sorted(lll10,reverse=True)
print(list3)
#sorts in disctionary order/asciee value
list3=['dfg','wdc','qwdfg']
print(list3.sort())
print(list3)

#l1=[1,24,5,3,'asd','hgfd','fdsert']
#print(l1.sort())#gives error

#sort by length
lst=['asdf',"wertyhg",'wertyj','qwertjbvfd']
lst.sort(key=len)
print(lst)
#based on first index
lst2=[[1,2,3,5],[6,4,8,9],[9,5,6,8]]
lst2.sort(key=lambda x:x[1])
print(lst2)
#based on first and second index
lst2=[[1,2,3,5],[6,4,8,9],[9,5,6,8]]
lst2.sort(key=lambda x:(x[1],x[2]))
print(lst2)

#11)copy= shallow copy an deep copy
#shallow copy changes also apply on originallist
l11=[1,24,5,3]
l111=l11
l111.append(48)
print(l111)
print(l11)
# deep copy = copy wont change the original,list
l12=[1,24,5,3]
ll12=l12.copy()
ll12.append(78)
print(ll12)
print(l12)

#string inbuilt methods
#.replace(old,new)=replace the old string with new one
s1='i love python'
print(s1.replace('python','coding'))
#strip=removes the space
s="   hellow world"
print(s.strip())
#1)find = used to find the letter or word that present in the given string and returns the index value if find
s1='praveen'
print(s1.find('p'))
print(s1.find('ee'))# o/p will be the index of first letter must match the total string
print(s1.find('P'))#if not found o/p will be -1
#2).startswith(" ")= used to find whether the given string startswith specific letter o/p will be T or F
s2='ambati'
print(s2.startswith('a'))#T
print(s2.startswith('amb'))#T
print(s2.startswith('m'))#F
print(s2.startswith('ambati'))#T
#3).endswith("")=used to find the list is ending with specific letter or pattern
s3='ambati praveen'
print(s3.endswith("n"))#T
print(s3.endswith("een"))#T
print(s3.endswith("a"))#F
print(s3.endswith("ambati praveen"))#T
#4).split()= will split the string in to saperate strings with out the given charactor
s4='ambati'
print(s4.split("a"))
print(s4.split('b'))
print(s4.split('i'))
#5)assigining two variables at a time with .split(" ") method
#str1=input("Enter csv formate:")
num1,num2=input("ENter number").split(",")
print(num1)
print(num2)
print(type(num1))#string
#6)converting to int
num1,num2,num3=map(int,input("Enter csv format").split(","))# for each map object we have given one variable so no need of mentioning list
print(num1)
print(type(num1))
#or
lst1=map(int,input("Enter csv format").split(","))
print(lst1)#<map object at 0x0000019BA2E66E30>
lst1=list(map(int,input("Enter csv format").split(",")))
print(lst1)
print('how are you'.split())
print('praveen'.split())
#6)join
lst6=['1','2','3','4']
print("".join(lst6))


#set
#1)add(element)=adds an elemnt to the set
set1={1,2}
set1.add(3)
print(set1)
#2 remove(element)=removes the specific element,reise error if not found
set2={1,2,3}
set2.remove(2)
print(set2)
#3)discord(element)=removes the element specified if not found wont rise the error
set3={1,2,3}
set3.discard(4)
print(set3)
#4)pop()=removes and returns an arbitary elements wont follow any order
set4={1,2,3}
print(set4.pop())#return the element
print(set4)
#5)celar()=empty the elemnt
set5={1,2,3}
set5.clear()
print(set5)
#6)union(other_set)=returns a set containing all elements from both sets
set6={1,2}
set66={2,3}
print(set6.union(set66))
#7)intersection(other_set)=returns elements common to both sets
set7={1,2,3}
set77={3,5,7}
print(set7.intersection(set77))
#8)difference(other_set)=returns elements in the first set but not in the second
set8={1,2}
set88={2,3}
print(set8.difference(set88))
#9)symmetric_difference(other-set)=returns elements in either set but not in both
set9={1,2}
set99={2,3}
print(set9.symmetric_difference(set9))
#10)issubset(other_set)=check all elements in set present in another set o/p will be T or F
set10={1,2,3}
set101={1,3,4}
print(set10.issubset(set101))
#11)issuperset(other_set)=checks if the set contains all elements of another set
set11={1,2,3}
set111={1,2}
print(set11.issuperset(set111))
#12)isdisjoint(other_set)=eeturns T if the sets have no elements in common
set12={1,2}
set112={3,4}
print(set12.isdisjoint(set112))












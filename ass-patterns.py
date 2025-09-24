n1=[
    [19,21,35,33,55],
    [54,67,73,55,33],
    [88,94,10,22,77],
    [84,93,10,22,77],
    [84,93,10,22,77]
]
'''n=5
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*", end=" ")
    print()'''


#A
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0 or j==0 or j == len(n1[i])-1 or i== len(n1) // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

# * * * * * 
# *       * 
# * * * * *
# *       *
# *       *

#B
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0 or j == len(n1[i])-1 or i== len(n1) // 2 or i==len(n1) -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

# * * * * * 
# *       * 
# * * * * *
# *       *
# * * * * *

#C
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0  or i==len(n1) -1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

# * * * * * 
# *
# *
# *
# * * * * *

#D
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0  or i==len(n1)-1 or j== len(n1[i])-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *

#E
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0  or i==len(n1)-1 or i== len(n1) // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

# * * * * * 
# *
# * * * * *
# *
# * * * * *

#F
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0   or i== len(n1) // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
# *
# * * * * *
# *
# *

#G
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j==0   or (i== len(n1) // 2  and j >= i )or i== len(n1)-1 or ( (j== len(n1[i])-1) and (len(n1)//2 <=i<=len(n1)-1) ) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
# *
# *   * * *
# *       *
# * * * * *

#H
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if   j==0   or (i== len(n1) // 2)or ( (j== len(n1[i])-1)) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# *       * 
# *       * 
# * * * * *
# *       *
# *       *

#I
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if i==0  or j == len(n1[i]) //2 or i==len(n1)-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
#     *     
#     *
#     *
# * * * * *

#J
'''for i in range(len(n1)):
    for j in range(len(n1)):
        if (i==0 and j < len(n1[i])//2) or j == len(n1[i]) //2 or (i==len(n1)-1 and j <= len(n1[i])//2):#if (i==0 and j < len(n1[i])-1) or j == len(n1[i]) //2 or i==len(n1)-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# * * *     
#     *     
#     *
#     *
# * * *

#K
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or i+j == 3  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# *     *   
# *   *     
# * *
# *
# *


#L
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or i== len(n1)-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# *
# *
# *
# *
# * * * * *

#M
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or j== len(n1[i])-1 or (i==j and i <= len(n1)//2) or (i+j==len(n1)-1 and  i <= len(n1)//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# *       * 
# * *   * * 
# *   *   *
# *       *
# *       *

#N
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or j== len(n1[i])-1 or i==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
# *       * 
# * *     * 
# *   *   *
# *     * *
# *       *

#O
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or i==0 or i== len(n1)-1 or j== len(n1[i])-1  :
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *

#P
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or (i==0 and j <= len(n1[i])//2 ) or (i == len(n1)//2 and j <= len(n1[i])//2) or (j== len(n1[i])//2 and i <= len(n1[i])//2):
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''
# * * *     
# *   *     
# * * *
# *
# *

#Q
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or (i==0 and j <= len(n1[i])//2 ) or (i == len(n1)//2 and j <= len(n1[i])//2) or (j== len(n1[i])//2 and i <= len(n1[i])//2):
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''

#R
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if j==0 or (i==0 and j <= len(n1[i])//2 ) or (i == len(n1)//2 and j <= len(n1[i])//2) or (j== len(n1[i])//2 and i <= len(n1[i])//2) or i-j == len(n1)//2:
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''
# * * *     
# *   *     
# * * *
# * *
# *   *

#S
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if (j==0 and i <= len(n1)//2 )or i==0  or i== len(n1)//2 or (j== len(n1[i])-1 and  i >= len(n1)//2) or i== len(n1)-1:
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''

# * * * * * 
# *
# * * * * *
#         *
# * * * * *

#T
'''for i in range(len(n1)):
    for j in range(len(n1)) :           
        if i==0 or j==2:
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()'''
# * * * * * 
#     *     
#     *
#     *
#     *

#U
for i in range(len(n1)):
    for j in range(len(n1)) :           
        if  j==0 or i== len(n1)-1 or j== len(n1[i])-1 :
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()
# *       * 
# *       * 
# *       *
# *       *
# * * * * *

#V
for i in range(len(n1)):
    for j in range(len(n1)) :           
        if  j==0 or i== len(n1)-1 or j== len(n1[i])-1 :
            print("*",end=" ")
       
        else:
            print(" ",end=" ")
    print()
#W,XYZ




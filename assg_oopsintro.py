class calculator:
    def add(self,a,b):
        print("addition of two numbers is:",a+b)
    def sub(self,a,b):
        print("subtraction of two numbers is:",a-b)
    def mul(self,a,b):
        if b!=0:
            print("multiplication of two numbers is:",a*b)
        else:
            print("Zero division error")
    def div(self,a,b):
        if b!=0:
            print("division of two numbers is:",a/b)
        else:
            print('ZeroDivisionError')
cal1=calculator()
cal1.model_num=1
cal1.made_in='india'
cal2=calculator()
cal2.color='red'
cal2.discount='10%'
cal1.add(2,1)
cal1.sub(2,1)
cal2.add(6,7)
print(cal1.model_num)
print(cal1.made_in)
print(cal2.color)
print(cal2.discount)


        
#oops=object oriented programming system or paradigm to overcome disadvantages in procisial programming like

#why oops=
#1 coad maintainability
#for example we write code to calculator we can write function to add,in the same file or imported from other file,if there is bug in your calculator you need to check all files which is not giving better code maintainability,whereas by using oops we write code in same file in structure
#2 data security, code exposure
# age=19 which is global variable can be access by anyone
#but some variables and functions need to be restricted which can be done by oops,like create 10 variables in a function and give function name to client ,so he can access all the variables with that no need to share info of all variables 
#ex:encapsulation,abstraction
#3 code reuse
#ex:inheritance


#vary fundamental to oops is 
#class and object
#class syn :class class_name:
# classmis the bile print of object and object is instance of class
# object=Real world entity(some property and behavior,functions ) class gives only the basic structure(like desighing a blueprint before making product)
#behaviour and data
#behaviour will be represented by functions called objects,functions written in class are called "methods"
#data will be represented by "variables"
#Methods
class Calculator:
    def add(self,a,b):#no need to give argumants to self its given by default
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self):
        #print(a*b)
        pass
    # def describe(self):
    #     print(clc1.id,clc1.manf_date)#if we dont mention clc1 here is an ambiguty for what object id shouls be print since we have many
    #     #here all bojects id and mnf date will returned as cls1 object id,mnf...,because describe is static to over come this
    # def describe(self):
    #     print(self.id,self.manf_date)#self is the reference variable refere the present object,this is why we use self as first perameter we can any name insted of self but in the first position only, but Suniversily represented by self
    
    
#we can create n objects for one structure(class)
clc1=Calculator()
clc2=Calculator()
clc3=Calculator()
#add(2,3) wrong way of using methods must give the ref of class
clc1.add(2,3)#used clc1 ref (boject) of class calculator
clc1.add(4,5)
clc1.add(6,99)
#clc1.describe()
#to distinguish objects we use variables see above all obj have same behaviour(methods or functions or functionalties) to distinguish them we use verables like distinguishing same company bike with number plate,owner name
#adding variables 
#1)manual way
#2)using constructor
#manual way
clc1.id=45
clc1.manf_date='01-sep-2025'
print(clc1.id)
print(clc1.manf_date)
clc2.manf_date="02-sep-2025"
#for example you have 1000 bojects for a structure(class) with 4 peremeters here you should give 4000 perametrs if you use manual way so we use constructure 
#2)using constructor=constructor is the mothod which will be called every time we create a object
#syn:def __init__(self):
class calcu:
    company_name='CASIO'
    def __init__(self,id1,mnf_date1,mrp1):
        self.id=id1
        self.mnf_date=mnf_date1
        self.mrp=mrp1
    def add(self,a,b):
        print(a+b)
    def describe(self):
        print(self.id,self.mnf_date)
    #method without any instance or class/static variables called staticmethod
    @staticmethod
    def connect_to_db(db_password,db_id):
        num1=10
        print("connect to database.....")
cal1=calcu(1,'01-sep-25',23)
cal2=calcu(2,'02-sep-25',23)
print(cal1.id,cal1.mnf_date)
print(cal1.id)


#types of variables=>instance variable,static/class variable
#types of methods=>instance methods ,static methods,class methods
# instance variable=>those variable valuse depend on an instance are called instance variables
#static/class variables=>these variables wont depend on instance but common to all object in that class
print(cal1.id)
#print(calcu.id)
#types of methods
# instance method=> any method which has atleast one instance variable is called instance method
class prav:
    def seshu(self,a,b):#instance method because self is a instance varaiable
        print(a+b)
        print(self.id)


@classmethod
# any method which has class or static variables
def change_company_name(cls,new_name):
    cls.company_name=new_name

#@staticmethod
#method without any instance or class/static variables called staticmethod
# def connect_to_db(db_password,db_id):
#     num1=10
#     print("connect to database.....")
cal4=calcu(2,'03-sep-25',24)
cal4.describe()
calcu.company_name=("new casio")
print(calcu.company_name)
#static
cal2.connect_to_db(1,3)
calcu.connect_to_db(2,5)

#decorators= decorators add additional functionality to existing functions

def example_decorator(func):
    def wrapper():
        print('checking requirments')
        func()
        print("thankyou")
    return wrapper

@example_decorator
def printer():
    print("printing in progress")
printer()

@example_decorator
def fax():
    print("fax in progress")
fax()

# 4 pillers of oops
#A P I E
#1 adstraction
#2 polymorfism
#3 inheritance
#4 encapsulation
#inheritance-why #
class cals:
    def add(self,a,b):
        print(a+b)
class adv_cal(cals):
    pass
    # def add(self,a,b):
    #     print(a+b)
obj=adv_cal
obj.add(2,2,3)

#inheritance
#single inheritance
# class a:
#     pass
# class b(a):
#     pass
# #multiple inheritance
# class a:
#     pass
# class b(a):
#     pass
# class c(a,b):
#     pass
# #hier
# class a:
#     pass
# class b(a):
#     pass
# class c(a):
#     pass
# #hydride
# class a:
#     pass
# class b(a):
#     pass
# class c:
#     pass
# class d(b,c):
#     pass

class vehical:
    company_name='TATA'
    def __init__(self,V_id,V_type):
            self.V_id=V_id
            self.V_type=V_type
            print(" vehical constructor")
    def drive(self):
        print("vehical in drive motion")
class car(vehical):
        def __init__(self, V_id, V_type):
             super().__init__(V_id, V_type)
             self.model_num=1234
             print(" car constructor")
        def drive(self):#here child class have same method as parent called method overriding
            super().drive()
            print("car in drive motion")
class bike(vehical):
    pass
class electric(car):
     pass
v1=vehical(22,34)
c1=car(34,67)
b1=bike(22,55)
c1.drive()
b1.drive()
v1.drive()
print(c1.company_name)
print(c1.model_num)
#multiple inheritance
class lion:
     def rore(self):
          print("tiger roring")
class tiger:
    def hunt(self):
          print(" tiger hunting")
    def rore(self):
        print("ligr roring") 
class ligr(lion,tiger):
     pass

lgr=ligr()
lgr.rore()# we have rore method in both classes will execute loin rore function because of inherting lion first called method resolution order
print(ligr.mro())



#polymorfism:any entity which showing different behiviours in different situvations
#three forms of polymorfism
#1)method overloading= can be indirectly achieved through arbitary argumants
# 2)method overriding
# 3)operator overlading
# 4)ducktyping#
#1) method overloading=same method name but with different perameters in same class
class addition:
    def add(self,a,b):#depend on number of perameters our function is performing in different ways called polymorfism
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
ad1=addition()
#2)methodoverriding=childclass having tha same function as parent class and when called that function child function will run
#depend on object implementation is changing the behieviour so called poli]y
class human:
    def talk(self):
        print("human is talking")
class student(human):
    def talk(self):
        print("student is talking with knowledge")
#why includede in polymorfism=line238
#where we use=if the child method required to rum differently than parent then we use overriding

#operator overloading=same operator performing different functionalties
2+ 3
'2'+'3'
[1,2,3]+[3,4,5,8]
#& integers bitwise in sets intersection
#why is it in poly morfism=+ changing operation deprnd on operators which is polymorfism
class marks:
    def __init__(self,sc_marks,so_marks,mat_marks):
        self.sc_marks=sc_marks
        self.so_marks=so_marks
        self.mat_marks=mat_marks
    def __add__(self,mark2):
        print(self.sc_marks+mark2.sc_marks)
        print(self.so_marks + mark2.so_marks)
        print(self.mat_marks + mark2.mat_marks)
    def __mul__(self,marks2):
        print("nen mul cheyanu")
        print(self.sc_marks + marks2.sc_marks)
    def __gt__(self,marks2):
        print(self.mat_marks < marks2.mat_marks)

mar1=marks(45,65,32)
mar2=marks(80,32,90)
print(mar1+mar2)
mar1>mar2
#4)duck typing= part of polymorfism which dosent care about datatype that we are passing,wont care about second method
class newmarks:
        def __init__(self,sc_marks,so_marks,mat_marks,eng_marks):
            self.sc_marks=sc_marks
            self.so_marks=so_marks
            self.mat_marks=mat_marks
            self.eng_marks=eng_marks
        def __add__(self,other):
            print(self.sc_marks+other.sc_marks)
            print(self.so_marks+other.so_marks)
            print(self.mat_marks+other.mat_marks)
            print(self.eng_marks+other.eng_marks)

nmc1=newmarks(35,75,91,25)
print(mar1+nmc1) #see here second argument is nmc1 but we dident write any __add__ method to cmc1 class but it is working based on mar1
# print((mar1). __add__ (nmc1))
# print(nmc1+mar1)

#encapsulation= hiding important data by  binding data with or using methods
class user:
    def __init__(self,user_name,password,age):
        self.user_name=user_name
        self.__password=password #private variable cant access out side the class to access we can create a method and use out side the class
        self._age=age#protected variable,in other prgm lang,protected variables can be used in class and sub class,but in python same as public variable,used just to givr an indication to the next coder
    def user_name1(self):
        print(self.user_name)
    def set_user_name(self,new_name):
        if type(new_name)!='str':
            return
        else:
            self.user_name=new_name
use1=user('werg','dfgh',23)
#given variable to user to access user_name
print(use1.user_name)
#with variable the user can change the actual user name he can read and write 
use1.user_name='changed'
# variable name not given
use1.user_name1()
use1.set_user_name("new")
#trying to change by using method name as varible name
print(use1.user_name)
use1.user_name='new1 name'#finally change
#to over come above we use access modifiers

#Access modifiers
#1)public variables=
#2)protected variables= _ in other prgm lang,protected variables can be used in class and sub class,but in python same as public variable,used just to givr an indication to the next coder
#3)private variables= __


#abstraction= hiding
#hiding implementation details of methods
#why abstraction= code modularity ,security

#abstract method= any method which dosent have any implementation is called abstractmethod
#abstract class=you cannot create any object to an abstract class
#theh why we created an abstract class if we cant create objact to expose a structure
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def show_details(ABC):
        pass
    def example_check(self):
        print("this is an example")
# atm1=ATM()
class Sbi_atm(ATM):
    def show_details(self):
        print("sbi implementation")
class ICICI:
    def show_details(self):
        print('ICICI implementation')

#distructor

class Vehical1:
    def __init__(self):
        print("constructor called")
    def __del__(self):
        print("deleted")
ob1=Vehical1()
del ob1




    



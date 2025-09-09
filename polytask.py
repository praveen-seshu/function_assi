#polymorfism
class Polymorfism:
    #method overloading
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
    def Ex_Method(self):
        print('Polymorfism method')
class Over_riding(Polymorfism):
    def Ex_Method(self):
        print('Over_riding mothod')
class Operator_overloading:
    def __init__(self,sc_marks,so_marks,mat_marks):
        self.sc_marks=sc_marks
        self.so_marks=so_marks
        self.mat_marks=mat_marks
    #overloading operator __add__
    def __add__(self,marks2):
        print(self.sc_marks + marks2.sc_marks)
        print(self.so_marks + marks2.so_marks)
        print(self.mat_marks + marks2.mat_marks)
ob_1=Operator_overloading(1,2,3)

class Operator_Overloading2:
    def __init__(self,sc_marks,so_marks,mat_marks):
        self.sc_marks=sc_marks
        self.so_marks=so_marks
        self.mat_marks=mat_marks
ob_2=Operator_Overloading2(4,5,6)
ob_1 + ob_2


            

        

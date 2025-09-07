class vehical:
    vehical_runs_on='ROAD'#ststic or class variable which does not depend on any instance
    vehical_contain='WHEELS'
    def __init__(self,vehical_number,color):# instance variables depend on an instance ,cant access without specifing the object,passed by using constructor
        self.vehica_number=vehical_number
        self.color=color
    def cycle(self):#instance method
        print("cycle running")
    def bike(self):
        print("bike running")
    @classmethod
    def car(cls,new_vehical_contain):
        cls.vehical_contain= new_vehical_contain
    @staticmethod
    def oredr(person_name,ph_number):
        print("order placed")
veh1=vehical(123,'blue')
print(veh1.color)
veh1.cycle()
veh1.person_name='jaohn'# manual way of assigning variables
veh1.ph_number=123456
veh1.car('2WHEELS')
print(vehical.vehical_contain)
vehical.new_vehical_contain='2WHEELS'
print(vehical.vehical_contain)

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:10:42 2019

@author: iA
"""

class employee:
    
    #class variables, shared among all instances
    raise_amount = 1.04
    num_of_emps = 0
    
    #regular methods take instance as the first argument
    def __init__(self,first,last,pay): #set for each instance, are called instance variables. can be unique for each instance
        self.first = first #self.first means that first is the instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        employee.num_of_emps += 1
     
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
# =============================================================================
#   using getter to make a method also run as an attribute
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first,self.last)
#     
# =============================================================================
#   
#     @fullname.setter
#     def fullname(self,name):
#       first,last = name.split...
#     
#     @fullname.deleter
#     
#     
#     
# =============================================================================
# =============================================================================
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
        #better to access class variables raise_amount through the instance(self) so that we can individually change for each instance
        
    #take class as the first argument    
    @classmethod #cls is used for class variable name - convention
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
        
    @classmethod #alternative constructor; convention to name them with 'from' at the start of the name
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod #static methods do not pass anything automatically, like regular functions but have some connection with the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#inheritance
class developer(employee):
    #can change anything here, parent class remains same
    raise_amount = 1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) # goes to parent class employee's init method
        self.prog_lang = prog_lang
        #can also use Employee.__init__(self,(first,last,pay)
        #but super() is better for multiple inheritance so always use super


class manager(employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
       if emp in self.employees:
           self.employees.remove(emp)        
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    
        
        

emp_1 = employee('Prakhar','Mehta',20000)
emp_2 = employee('Test','User',5000)

dev_1 = developer('Prakhar','Mehta',20000,'Python')

mgr_1 = manager('Sue','Smith',80000,[dev_1])

#useful functions to check when using 
#issubclass
#isinstance 

#for making outputs better understandable
repr(emp_1) #for debugging
str(emp_1)
print(emp_1)
# =============================================================================
# 
# print(dev_1.prog_lang)
# print(dev_1.email)
# 
# =============================================================================
# =============================================================================
# 
# mgr_1 = manager('Sue','Smith',80000,[dev_1])
# print(mgr_1.email)
# 
# mgr_1.print_emps()
# 
# mgr_1.add_emp(emp_2)
# mgr_1.print_emps()
# # =============================================================================
# =============================================================================
# 
# import datetime
# my_date = datetime.date(2016,7,10)
# 
# print(employee.is_workday(my_date))
# 
# =============================================================================
#employee.set_raise_amount(1.05) #this is the same as setting the class variable manually by doing: employee.raise_amount = 1.05

#print(employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#emp_str_1 = 'john-oliver-2000'

#first, last, pay = emp_str_1.split('-')

#new_emp_1 = employee.from_string(emp_str_1)

#print(new_emp_1.email)

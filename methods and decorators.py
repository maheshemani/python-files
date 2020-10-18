# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:39:03 2020

@author: mahesh.emani
"""

"""
class method vs object method
"""

class snake:
    legs = 'no'
    def __init__(self,species,length,color,venom):
        self.species=species
        self.length=length
        self.color=color
        self.venom=venom        
    @classmethod #called decorator and is needed to access class variable
    def legdetails(cls):
        print(cls.legs)
    # instance method
    def snek_detail(self):
        print(self.species,self.length,self.color,self.venom)
    @staticmethod
    def snek_warning():
        print("danger noodle")
        

snake1=snake('anaconda',10,'white','yes')        

snake1.legs        
snake1.legdetails()
snake.snek_warning()

########################################################
"""class in a class"""

class reptile:
    legs = 'maybe'
    blood = 'cold'
    
    def __init__(self,species,scales,issnek):
        self.species=species
        self.scales=scales
        self.snek=self.snake(issnek)
        
    class snake:
        legs = 'no'
        def __init__(self,issnek):
            self.issnek=issnek
            self.species='NA'
            self.length=0
            self.color='NA'
            self.venom='NA'
       
        @classmethod #called decorator and is needed to access class variable
        def legdetails(cls):
            print(cls.legs)
        # instance method
        def snek_detail(self):
            print(self.species,self.length,self.color,self.venom)
        @staticmethod
        def snek_warning():
            print("danger noodle")
    
    def rept_details(self):
        print("species: " ,self.species)
        print("\n scales: ", self.scales)
        print("\n is snek:", self.snek.issnek)
        print("\n warning:" ,self.snek.snek_warning())

croc = reptile('crocodile','yes','no')
croc.legs
croc.blood
croc.rept_details()

# accessing subclass variables using subclass name 'snake' directly
croc.snake.legs
croc.snake.snek_warning()
croc.snake.legdetails()

reptile.snake.legdetails()

"""the below line throws an error.Why?
    snek_detail() is an instance method and 'snek' is the actual instance not 'snake' """

croc.snake.snek_detail()


# accessing subclass variables using subclass instance 'snek' directly
croc.snek.legs
croc.snek.snek_warning()
croc.snek.legdetails()
croc.snek.snek_detail()








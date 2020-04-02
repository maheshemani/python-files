# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:15:58 2020

@author: mahesh.emani
"""

class book:
    def name(self):        
        print("book name")

""" Q1.below we instantiate the class book
    Q2.how do i create a new instance with more custom attributes?"""        
book1 = book()
book2 = book()

"""the 2 ways of getting the details of the book"""  
#1
book.name(book1)
book.name(book2)

#2 when we call the name method, we didn't specify any parameter and the method takes book1 directly because of 'self'
book1.name()
book2.name()

################

"""note that the fn can be defined without self but instantiation can't happen without using self"""

class book:
    def name():        
        print("book name")
#using the function based on the class name
book.name()
        
book1 = book()
book2 = book() 
#1
book.name(book1)
book.name(book2)
#2 
book1.name()
book2.name()


"""
In the case where 'self' was used and book1 was defined as an instance, the function understands that there
is no need for an additional input parameter.

However, in the latter case, we see the following error:
    TypeError: name() takes 0 positional arguments but 1 was given
"""

##################################################

class book_custom:
    def __init__(self,name,author,pages):
        """this segment acts as a constructor
           it helps us solve the problem in Q2
           we define all the properties/attributes a book can have 
           when a new object is instantiated with various properties, we can directly mention them in the call"""
        self.name=name
        self.author=author
        self.pages=pages
           
    def details(self):
        """here we need self.name as the method can't directly understand what name is
           Q3. Why is the above statement true?
           Q4. How do I specify the data types of input attributes? """
        print("book name: ",self.name)
        print("\n author: ",self.author)
        print("\n pages: ",self.pages)
    
book3 = book_custom("LOTR","JRR",1000)
book3.details()

#################################################
#class variable and instance variable

class book_custom2:
    made_of = 'paper'
    def __init__(self,name,author,pages):
        """this segment acts as a constructor
           it helps us solve the problem in Q2
           we define all the properties/attributes a book can have 
           when a new object is instantiated with various properties, we can directly mention them in the call"""
        self.name=name
        self.author=author
        self.pages=100
           
    def details(self):
        """here we need self.name as the method can't directly understand what name is
           Q3. Why is the above statement true?
           Q4. How do I specify the data types of input attributes? """
        print("book name: ",self.name)
        print("\n author: ",self.author)
        print("\n pages: ",self.pages)

book4 = book_custom2("GoT","GRR",10)
book4.details() # notice that the output has 100 pages
book5 = book_custom2("Mybook","Me",111)
book5.details() # notice that the output has 100 pages

book4.pages =10
book4.details() # now the pages is 10
book5.details() # book 5 is un affected 

"""what do I do to have a variable that gets affected for multiple objects?
   A:the sol is to change the value in class namespace"""
book4.made_of
book5.made_of

book_custom2.made_of = 'electronic'

# below we see that the value changes for both the objects
book4.made_of
book5.made_of

#######################################################################################

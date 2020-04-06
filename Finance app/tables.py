# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:28:33 2019

@author: mahesh.emani
"""
from datetime import datetime
from myapp import db
#from flask_table import Table, Col

class User(db.Model):
    __tablename__ = "User"
    rowid=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer,nullable=False,unique=False)
    name=db.Column(db.String(100),nullable=False,unique=False)
    email=db.Column(db.String(100),nullable=False,unique=False)
    billtype=db.Column(db.String(100),nullable=False,unique=False)
    amount=db.Column(db.Integer,nullable=False,unique=False)
    billdoc=db.Column(db.String(100),nullable=True,unique=False)
    
    def __represent__(self):
        return f"User('{self.rowid}','{self.uid}','{self.name}','{self.email}','{self.billtype}','{self.amount}','{self.billdoc}')"


class Requests(db.Model):
    uid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    billtype=db.Column(db.String(100),nullable=False)
    amount=db.Column(db.Integer,nullable=False)
    billdoc=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.date)
    
    def __represent__(self):
        return f"User('{self.uid}','{self.name}','{self.email}','{self.billtype}','{self.amount}','{self.billdoc}','{self.date_posted}')"



# =============================================================================
# class Results(Table):
#     email = Col('email', show=False)
#     username = Col('username')
#     id = Col('id')
#     billtype = Col('billtype')
#     bill = Col('bill')
#     amount = Col('amount')
#     def __names__(self):
#         return f"User('{self.email}','{self.username}','{self.id}','{self.billtype}','{self.bill}','{self.amount}')"
#     
#     
# =============================================================================
    
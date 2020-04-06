# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:18:29 2019

@author: mahesh.emani
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""the application is 'captured(instantiated)' by the variable app"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)




from myapp import basefunctions
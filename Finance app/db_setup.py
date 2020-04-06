# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:56:16 2019

@author: mahesh.emani
"""

# db_setup.py
 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
engine = create_engine('sqlite:///site.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
 

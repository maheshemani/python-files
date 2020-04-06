# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
from flask import  render_template, request, redirect, url_for, flash
from myapp.tables import User,Requests
from myapp import app, db
from flask_table import Table, Col
from sqlalchemy import create_engine


""" URL to reach our page is defined below"""
@app.route('/',methods = ['GET','POST'])
@app.route('/home',methods = ['GET','POST'])
def home_page():
    #return "<h1>mein Flask ist fertig!</h1>" 
    return render_template('employee interface.html') 
"""the above line needs us to create a folder called 'templates' 
   the html file needs to be saved there"""


info=[]

@app.route('/userinfo', methods = ['GET','POST'])
def user_info():
    username = request.form['username']
    uid = request.form['id']
    b_type = request.form['billtype']
    #bill = request.form['bill']
    amount = request.form['amount']
    email = request.form['email']
    #details = [username,email,uid,b_type,amount]
    info.append(email)
    info.append(username)
    info.append(uid)
    info.append(b_type)
    info.append(amount)
    #info.append(bill)
    #user=User(uid=uid,name=username,email=email,billtype=b_type,amount=amount,billdoc=bill)
    #db.session.add(user)
    #db.session.commit()
    #if request.method == 'POST':
    #    result = request.form
    #flash('Submission successful!')
    #return redirect(url_for('home_page'))
    
    return "<h1>Submitted!</h1>"



# =============================================================================
@app.route('/mgrinterface', methods = ['GET','POST'])
def mgr_page():
    #return render_template('mgrui2.html', info=info)
    #status=request.form['Status']
    #info.append(status)
    #return "<h1>Submitted!</h1>"
    return render_template("mgrinterface.html",info = info)
# =============================================================================
@app.route('/mgrui2', methods = ['GET','POST'])
def mgr_conf():
    #status=request.form['status']
    status = "Accepted"
    return render_template('mgrui2.html', status=status)
#    return render_template("mgrinterface.html",info = info)
        
# =============================================================================
# =============================================================================
# @app.route('/finui', methods = ['GET','POST'])
# def fin_page():
#     #status=request.form['status']
#     return render_template("mgrinterface.html",info = info)    
# =============================================================================



# details1 = ['Mahesh','503']
# 
# @app.route('/mgrinterface', methods = ['GET','POST'])
# def mgr_ux():
#     return render_template('mgr interface.html',info=details1) 
# 
# =============================================================================




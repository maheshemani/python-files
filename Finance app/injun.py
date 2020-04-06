# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:58:36 2019

@author: mahesh.emani
"""


@app.route('/mgrui')
def articles():
    engine = create_engine('sqlite:///site.db')
    connection = engine.connect()

# Get all the rows from the sql database table named data

    result = connection.execute("SELECT * FROM User")

    if result > 0:
        return render_template('mgrui.html', data=result)
    else:
        msg = 'No Data Found'
        return render_template('mgrui.html', msg=msg)
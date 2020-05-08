"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify, make_response
from FlaskWebProject1 import app
import pyodbc





@app.route('/')
def toGoMain():
    return render_template(
        'Main.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/toAddEmp')
def toAddEmp():
    return render_template(
        'Form.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/delEmp')
def delEmp():
    return render_template(
        'delete.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/showEmp')
def showEmp():
    conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};" #????
    "Server=LAPTOP-FH7RGJ13\SQLEXPRESS;"
    "Database=Proj2020;"
    "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute("select FNAME, LNAME, JOBID from Employees")
    l_emp=[]
    #for i in l_emp:
    # print(i)
    #l_emp.append(row)
    for row in cursor:
        l_emp.append(str(row))
    print()
    conn.close()
    return render_template(
        'Show.html',
        title='Home Page', # list of Employees
        year=datetime.now().year,
        list_of_emp=l_emp,
        list_length=len(l_emp),

    )

@app.route('/fromFieldsEmp', methods=['POST'])
def fromFieldsEmp():
    conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};" #????
    "Server=LAPTOP-FH7RGJ13\SQLEXPRESS;"
    "Database=Proj2020;"
    "Trusted_Connection=yes;"
    )
    employee_name = request.form.get('name')
    employee_surname = request.form.get('surname')
    employee_minsalary = request.form.get('minsalary')  # access the data inside 
    employee_maxsalary = request.form.get('maxsalary')
    employee_jobid = request.form.get('jobid')
    cursor = conn.cursor()
    cursor.execute(
        'insert into Employees(FNAME, LNAME, MINSALARY, MAXSALARY, JOBID) values(?,?,?,?,?);',
        (employee_name, employee_surname, float(employee_minsalary), float(employee_maxsalary), int(employee_jobid))
    )
    conn.commit()
    conn.close()
    return render_template(
        'Main.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/delEmpDB', methods=['POST'])
def delEmpDB():
    conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};" #????
    "Server=LAPTOP-FH7RGJ13\SQLEXPRESS;"
    "Database=Proj2020;"
    "Trusted_Connection=yes;"
    )
    employee_name = request.form.get('name')
    employee_surname = request.form.get('surname')
    employee_jobid = request.form.get('jobid')
    cursor = conn.cursor()
    var_del='delete from Employees where FNAME=\'' + employee_name + '\' and LNAME=\'' + employee_surname + '\' and JOBID=' + employee_jobid
    print(var_del)
    cursor.execute(
        var_del
    )
    conn.commit() 
    conn.close()
    return render_template(
        'Main.html',
        title='Home Page',
        year=datetime.now().year,
    )

  



  
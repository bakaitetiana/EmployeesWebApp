# EmployeesWebApp
A web application that displays a list of employees, lets you add a new employee and remove an existing employee 


Web application for the project was developed in Flask on Visual Studio. It is a micro web framework written in Python. 


So, project contains the following files:
o	Main.html
o	Form.html 
o	Delete.html
o	Show.html
o	Style.css
o	View.py


Once I run the project in VS, it automatically opens the content of Main.html  on browser. On this page user can see three buttons: Add, Delete and Show Employees. Once we click on button “Add”, forms for adding the employee would appear (Form.html). Same thing will happen once the user clicks on the button “Delete”. The forms for deleting the Employee are written in Delete.html. 

View.py contains the following controllers:
•	toGoMain (returns Main.html)
•	toAddEmp (returns Form.html)
•	delEmp (returns delete.html)
•	fromFieldsEmp (inserts all data from fields into the DB)
•	showEmp (connects with DB, selects all employees and prints them on the web page)
•	delEmpDB (takes all data from fields and deletes the record from the DB)

Also, it is necessary to import pyodbc module in Python script to connect the web page to the database. Once the connection was opened, it is necessary to close it after the action has been completed by conn.close().
Table Employees was created in SQL Server Management Studio.

##Employee Management System

This is a comprehensive Employee Management System developed using Python and Tkinter with MySQL for database management. It allows users to manage employee records, including adding, updating, deleting, and searching for employees. The system features a user-friendly graphical interface for easy interaction.

##Screenshots
![Login Page](login.png)
![main field](mainfield.png)

##Features

User authentication with login functionality.
Add, update, delete, and search employee records.
View all employee records in a table.
Delete all records with a single click.
Responsive interface with real-time updates.

##Installation
 1 Clone the repository:

git clone https://github.com/Coder-786hub/Employee-Management-System.git

##Change into the project directory:

cd Employee-Management-System

##Install the required Python packages:


pip install -r requirements.txt

##Ensure MySQL is installed and running. Replace 'your_password' in database.py with your MySQL root password.

##Create the database and table by running:


python database.py
Running the Application
Run the main application script:


python main.py

###The application window will appear. Use the login credentials to access the employee management interface.

##Files

main.py: The main Python script for the application with the login and main interface.
database.py: Script for creating the database and tables and handling CRUD operations.
requirements.txt: List of required Python packages.
login_page.png, employee_management.png: Screenshots of the application.

##License

This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgements

MySQL for database management.
Tkinter for the graphical user interface.
CustomTkinter for enhanced Tkinter widgets.
Pillow for image handling.

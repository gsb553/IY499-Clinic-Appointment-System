CLINIC APPOINTMENT MANAGEMENT SYSTEM

Name: Esosa Bangira
Student Number: 303070741
Module Code: IY499
Module Name: Introduction to Programming


DECLARATION OF OWN WORK

I confirm that this assignment is my own work.
Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.


PROGRAM DESCRIPTION

The Clinic Appointment Management System is a text-based Python application designed to help a small clinic organise and manage patient appointments. The program allows the user to add, view, search, sort, edit and delete appointment records. The user can also update an appointment’s status to Booked, Completed or Cancelled.

Appointment information is stored using a list of dictionaries. Each appointment contains a unique ID, patient name, patient age, doctor name, reason for the appointment, date, time and status. The program uses a linear search algorithm to locate appointments and a bubble sort algorithm to arrange records by date and time, patient name, doctor name or status.

The program can save appointment records to an appointments.csv file and load them again when it is reopened. It includes input validation for names, ages, dates, times and menu choices. It also prevents active double bookings and safely handles missing or invalid file data. Recursion is used to count appointments, while a text-based bar chart provides a summary of appointment statuses.


FEATURES

- Add new appointments
- View all appointments
- Search for appointments
- Sort appointments using bubble sort
- Edit existing appointment details
- Update appointment statuses
- Delete appointments
- Save records to a CSV file
- Load records from a CSV file
- Prevent active doctor double bookings
- Validate user input and recover from errors
- Display an appointment summary using a text-based chart


PACKAGES AND LIBRARIES USED

The following Python standard libraries are used:

- csv
- os
- datetime

These libraries are included with Python. No external packages or requirements.txt file are required.


PROJECT FILES

The project folder should contain:

- main.py
- appointments.csv
- README.txt


INSTALLATION INSTRUCTIONS

1. Install Python 3 on the computer.
2. Download and unzip the project folder.
3. Make sure main.py, appointments.csv and README.txt are stored in the same folder.
4. Open Visual Studio Code.
5. Select File, then Open Folder.
6. Choose the IY499_Clinic_Appointment_System folder.
7. Open a new terminal in Visual Studio Code by selecting Terminal, then New Terminal.


HOW TO RUN THE PROGRAM

In the Visual Studio Code terminal, enter:

python3 main.py

Press Enter to start the program.

The main menu will appear. Enter the number of the required option and follow the instructions displayed on the screen.

Use option 8 to save appointments manually.

Use option 0 to save all appointments and exit the program safely.


DATA FILE

Appointment records are stored in:

appointments.csv

The CSV file must remain in the same folder as main.py. The program automatically loads existing appointment records when it starts and saves records when the user selects the save option or exits safely.


REPOSITORY LINK

https://github.com/gsb553/IY499-Clinic-Appointment-System
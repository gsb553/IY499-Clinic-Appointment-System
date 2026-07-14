CLINIC APPOINTMENT MANAGEMENT SYSTEM

Name: Esosa Bangira
Student Number: 303070741
Course Code: IY499
Module: Introduction to Programming

DECLARATION OF OWN WORK

I confirm that this assignment is my own work.
Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.

PROGRAM DESCRIPTION

The Clinic Appointment Management System is a text-based Python application designed to help a small clinic manage patient appointments. The user can add, view, search, sort, edit and delete appointment records. Appointment statuses can also be changed to booked, completed or cancelled.

The program stores appointment information using a list of dictionaries. Each record contains an appointment ID, patient details, doctor name, reason, date, time and status. A linear search algorithm is used to find records, while a bubble sort algorithm arranges appointments by date, patient name, doctor name or status.

Appointment data can be saved to and loaded from a CSV file. The program checks user input, rejects impossible dates and times, prevents active double bookings and handles invalid file data without crashing. A recursive function is used to count appointments, and a text-based chart displays an appointment summary.

PACKAGES AND LIBRARIES USED

csv
os
datetime

These are included with Python, so no external packages are required.

INSTALLATION INSTRUCTIONS

1. Install Python 3.
2. Download and unzip the project folder.
3. Open Terminal and move into the project folder.

HOW TO RUN

Run:

python3 main.py

REPOSITORY LINK

https://github.com/gsb553/IY499-Clinic-Appointment-System
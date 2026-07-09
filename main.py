# Clinic Appointment Management System
# IY499 Introduction to Programming
# A first-year Python project using lists, dictionaries, files, searching and sorting

import csv
import os

FILE_NAME = "appointments.csv"

appointments = []
next_appointment_id = 1


def show_menu():
    print("\n===================================")
    print("   Clinic Appointment Management")
    print("===================================")
    print("1. Add appointment")
    print("2. View all appointments")
    print("3. Search appointment by patient name")
    print("4. Sort appointments")
    print("5. Update appointment status")
    print("6. Save appointments to file")
    print("7. Load appointments from file")
    print("8. Show appointment summary")
    print("0. Exit")


def get_non_empty_input(message):
    while True:
        user_input = input(message).strip()

        if user_input != "":
            return user_input

        print("This cannot be empty. Please try again.")


def get_valid_age():
    while True:
        age = input("Enter patient age: ").strip()

        if age.isdigit():
            age = int(age)

            if age >= 1 and age <= 120:
                return age

            print("Age must be between 1 and 120.")
        else:
            print("Please enter a number.")


def get_valid_date():
    while True:
        date = input("Enter appointment date (DD/MM/YYYY): ").strip()
        parts = date.split("/")

        if len(parts) == 3:
            day = parts[0]
            month = parts[1]
            year = parts[2]

            if day.isdigit() and month.isdigit() and year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)

                if day >= 1 and day <= 31 and month >= 1 and month <= 12 and year >= 2026:
                    return date

        print("Please enter a valid date, for example 22/07/2026.")


def get_valid_time():
    while True:
        time = input("Enter appointment time (HH:MM): ").strip()
        parts = time.split(":")

        if len(parts) == 2:
            hour = parts[0]
            minute = parts[1]

            if hour.isdigit() and minute.isdigit():
                hour = int(hour)
                minute = int(minute)

                if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
                    return time

        print("Please enter a valid time, for example 14:30.")


def pause_program():
    input("\nPress Enter to continue...")


def add_appointment():
    global next_appointment_id

    print("\nAdd New Appointment")

    patient_name = get_non_empty_input("Enter patient name: ")
    patient_age = get_valid_age()
    doctor_name = get_non_empty_input("Enter doctor name: ")
    reason = get_non_empty_input("Enter reason for appointment: ")
    date = get_valid_date()
    time = get_valid_time()

    appointment = {
        "id": next_appointment_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "doctor_name": doctor_name,
        "reason": reason,
        "date": date,
        "time": time,
        "status": "Booked"
    }

    appointments.append(appointment)
    next_appointment_id = next_appointment_id + 1

    print("\nAppointment added successfully.")


def display_one_appointment(appointment):
    print("\n-----------------------------------")
    print("Appointment ID:", appointment["id"])
    print("Patient Name:", appointment["patient_name"])
    print("Patient Age:", appointment["patient_age"])
    print("Doctor:", appointment["doctor_name"])
    print("Reason:", appointment["reason"])
    print("Date:", appointment["date"])
    print("Time:", appointment["time"])
    print("Status:", appointment["status"])


def view_all_appointments():
    print("\nAll Appointments")

    if len(appointments) == 0:
        print("No appointments have been added yet.")
        return

    for appointment in appointments:
        display_one_appointment(appointment)


def search_appointments():
    print("\nSearch Appointment")

    if len(appointments) == 0:
        print("There are no appointments to search.")
        return

    search_name = get_non_empty_input("Enter patient name to search for: ").lower()
    found = False

    # Linear search: checks each appointment one by one
    for appointment in appointments:
        if search_name in appointment["patient_name"].lower():
            display_one_appointment(appointment)
            found = True

    if found == False:
        print("No matching appointment was found.")


def get_date_for_sorting(date_text):
    parts = date_text.split("/")

    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])

    return year, month, day


def bubble_sort_appointments(sort_choice):
    sorted_list = appointments.copy()

    # Bubble sort is used here because it is simple to understand at first-year level
    for i in range(len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):

            first = sorted_list[j]
            second = sorted_list[j + 1]

            if sort_choice == "1":
                first_value = get_date_for_sorting(first["date"])
                second_value = get_date_for_sorting(second["date"])
            elif sort_choice == "2":
                first_value = first["patient_name"].lower()
                second_value = second["patient_name"].lower()
            else:
                first_value = first["doctor_name"].lower()
                second_value = second["doctor_name"].lower()

            if first_value > second_value:
                sorted_list[j] = second
                sorted_list[j + 1] = first

    return sorted_list


def sort_appointments():
    print("\nSort Appointments")

    if len(appointments) == 0:
        print("There are no appointments to sort.")
        return

    print("1. Sort by date")
    print("2. Sort by patient name")
    print("3. Sort by doctor name")

    choice = input("Choose sorting option: ").strip()

    if choice == "1" or choice == "2" or choice == "3":
        sorted_appointments = bubble_sort_appointments(choice)

        print("\nSorted Appointments")
        for appointment in sorted_appointments:
            display_one_appointment(appointment)
    else:
        print("Invalid sorting option.")


def find_appointment_by_id(appointment_id):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    return None


def update_status():
    print("\nUpdate Appointment Status")

    if len(appointments) == 0:
        print("There are no appointments to update.")
        return

    view_all_appointments()

    appointment_id = input("\nEnter the appointment ID to update: ").strip()

    if appointment_id.isdigit() == False:
        print("Please enter a valid appointment ID.")
        return

    appointment_id = int(appointment_id)
    appointment = find_appointment_by_id(appointment_id)

    if appointment == None:
        print("Appointment ID was not found.")
        return

    print("\nChoose new status:")
    print("1. Booked")
    print("2. Completed")
    print("3. Cancelled")

    status_choice = input("Choose an option: ").strip()

    if status_choice == "1":
        appointment["status"] = "Booked"
    elif status_choice == "2":
        appointment["status"] = "Completed"
    elif status_choice == "3":
        appointment["status"] = "Cancelled"
    else:
        print("Invalid status option.")
        return

    print("Appointment status updated.")


def save_appointments():
    field_names = [
        "id",
        "patient_name",
        "patient_age",
        "doctor_name",
        "reason",
        "date",
        "time",
        "status"
    ]

    try:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(appointments)

        print("\nAppointments saved to", FILE_NAME)

    except:
        print("\nAn error happened while saving the file.")


def load_appointments():
    global appointments
    global next_appointment_id

    if os.path.exists(FILE_NAME) == False:
        print("\nNo saved appointments file was found.")
        return

    loaded_appointments = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                appointment = {
                    "id": int(row["id"]),
                    "patient_name": row["patient_name"],
                    "patient_age": int(row["patient_age"]),
                    "doctor_name": row["doctor_name"],
                    "reason": row["reason"],
                    "date": row["date"],
                    "time": row["time"],
                    "status": row["status"]
                }

                loaded_appointments.append(appointment)

        appointments = loaded_appointments

        if len(appointments) > 0:
            highest_id = 0

            for appointment in appointments:
                if appointment["id"] > highest_id:
                    highest_id = appointment["id"]

            next_appointment_id = highest_id + 1
        else:
            next_appointment_id = 1

        print("\nAppointments loaded successfully.")

    except:
        print("\nThe file could not be loaded correctly.")


def count_appointments_recursively(index):
    # Recursion: the function calls itself until it reaches the end of the list
    if index == len(appointments):
        return 0

    return 1 + count_appointments_recursively(index + 1)


def count_status(status_name):
    count = 0

    for appointment in appointments:
        if appointment["status"] == status_name:
            count = count + 1

    return count


def show_bar(label, amount):
    print(label + ":", "*" * amount, "(" + str(amount) + ")")


def show_summary():
    print("\nAppointment Summary")

    total = count_appointments_recursively(0)
    booked = count_status("Booked")
    completed = count_status("Completed")
    cancelled = count_status("Cancelled")

    print("Total appointments:", total)
    print("\nStatus Chart")
    show_bar("Booked   ", booked)
    show_bar("Completed", completed)
    show_bar("Cancelled", cancelled)


def main():
    load_appointments()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_appointment()
            pause_program()
        elif choice == "2":
            view_all_appointments()
            pause_program()
        elif choice == "3":
            search_appointments()
            pause_program()
        elif choice == "4":
            sort_appointments()
            pause_program()
        elif choice == "5":
            update_status()
            pause_program()
        elif choice == "6":
            save_appointments()
            pause_program()
        elif choice == "7":
            load_appointments()
            pause_program()
        elif choice == "8":
            show_summary()
            pause_program()
        elif choice == "0":
            save_appointments()
            print("Thank you for using the Clinic Appointment Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")
            pause_program()


main()
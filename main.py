# Clinic Appointment Management System
# IY499 Introduction to Programming
# Version 1: basic menu, add appointments and view appointments

appointments = []
next_appointment_id = 1


def show_menu():
    print("\n==============================")
    print("  Clinic Appointment System")
    print("==============================")
    print("1. Add a new appointment")
    print("2. View all appointments")
    print("3. Search appointments")
    print("4. Sort appointments")
    print("5. Save appointments")
    print("6. Load appointments")
    print("0. Exit")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value
        else:
            print("This field cannot be empty. Please try again.")


def get_patient_age():
    while True:
        age = input("Enter patient age: ").strip()

        if age.isdigit():
            age = int(age)

            if age > 0 and age <= 120:
                return age
            else:
                print("Age must be between 1 and 120.")
        else:
            print("Please enter a valid number for age.")


def add_appointment():
    global next_appointment_id

    print("\nAdd New Appointment")

    patient_name = get_non_empty_input("Enter patient name: ")
    patient_age = get_patient_age()
    doctor_name = get_non_empty_input("Enter doctor name: ")
    appointment_reason = get_non_empty_input("Enter reason for appointment: ")
    appointment_date = get_non_empty_input("Enter date, for example 22/07/2026: ")
    appointment_time = get_non_empty_input("Enter time, for example 14:30: ")

    appointment = {
        "id": next_appointment_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "doctor_name": doctor_name,
        "reason": appointment_reason,
        "date": appointment_date,
        "time": appointment_time,
        "status": "Booked"
    }

    appointments.append(appointment)
    next_appointment_id += 1

    print("Appointment added successfully.")


def view_appointments():
    print("\nAll Appointments")

    if len(appointments) == 0:
        print("There are no appointments saved yet.")
        return

    for appointment in appointments:
        print("\n------------------------------")
        print("Appointment ID:", appointment["id"])
        print("Patient Name:", appointment["patient_name"])
        print("Patient Age:", appointment["patient_age"])
        print("Doctor:", appointment["doctor_name"])
        print("Reason:", appointment["reason"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Status:", appointment["status"])


def search_appointments():
    print("\nSearch feature will be added in the next version.")


def sort_appointments():
    print("\nSort feature will be added in the next version.")


def save_appointments():
    print("\nSave feature will be added in the next version.")


def load_appointments():
    print("\nLoad feature will be added in the next version.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            search_appointments()
        elif choice == "4":
            sort_appointments()
        elif choice == "5":
            save_appointments()
        elif choice == "6":
            load_appointments()
        elif choice == "0":
            print("Thank you for using the Clinic Appointment System.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")


main()
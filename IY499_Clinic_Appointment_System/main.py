# Clinic Appointment Management System
# IY499 Introduction to Programming
# This program uses functions, lists, dictionaries, CSV files,
# searching, sorting, recursion, validation and a text-based interface.

import csv
import os
from datetime import date, datetime


FILE_NAME = os.path.join(os.path.dirname(__file__), "appointments.csv")
FIELD_NAMES = [
    "id",
    "patient_name",
    "patient_age",
    "doctor_name",
    "reason",
    "date",
    "time",
    "status"
]
VALID_STATUSES = ["Booked", "Completed", "Cancelled"]

appointments = []
next_appointment_id = 1


def show_menu():
    """Display the main menu."""
    print("\n========================================")
    print("   CLINIC APPOINTMENT MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add appointment")
    print("2. View all appointments")
    print("3. Search appointments")
    print("4. Sort appointments")
    print("5. Edit appointment")
    print("6. Update appointment status")
    print("7. Delete appointment")
    print("8. Save appointments to file")
    print("9. Load appointments from file")
    print("10. Show appointment summary")
    print("0. Save and exit")


def pause_program():
    """Pause the program so the user can read the output."""
    input("\nPress Enter to continue...")


def get_non_empty_input(message):
    """Return an input that is not empty."""
    while True:
        user_input = input(message).strip()

        if user_input:
            return user_input

        print("This field cannot be empty. Please try again.")


def get_valid_name(message):
    """Return a name containing sensible name characters."""
    while True:
        name = get_non_empty_input(message)
        allowed_characters = " -'."

        if all(character.isalpha() or character in allowed_characters for character in name):
            return " ".join(name.split())

        print("Please use letters, spaces, hyphens or apostrophes only.")


def get_valid_age():
    """Return a patient age between 0 and 120."""
    while True:
        age_text = input("Enter patient age: ").strip()

        try:
            age = int(age_text)

            if 0 <= age <= 120:
                return age

            print("Age must be between 0 and 120.")
        except ValueError:
            print("Please enter the age as a whole number.")


def get_valid_date(message="Enter appointment date (DD/MM/YYYY): ", allow_past=False):
    """Return a real date in DD/MM/YYYY format."""
    while True:
        date_text = input(message).strip()

        try:
            appointment_date = datetime.strptime(date_text, "%d/%m/%Y").date()

            if not allow_past and appointment_date < date.today():
                print("The appointment date cannot be in the past.")
            else:
                return appointment_date.strftime("%d/%m/%Y")

        except ValueError:
            print("Please enter a real date, for example 22/07/2026.")


def get_valid_time(message="Enter appointment time (HH:MM): "):
    """Return a real 24-hour time in HH:MM format."""
    while True:
        time_text = input(message).strip()

        try:
            appointment_time = datetime.strptime(time_text, "%H:%M")
            return appointment_time.strftime("%H:%M")
        except ValueError:
            print("Please enter a valid 24-hour time, for example 14:30.")


def find_appointment_by_id(appointment_id):
    """Use a linear search to find an appointment by its ID."""
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment

    return None


def get_valid_appointment_id(message):
    """Return an existing appointment ID, or None if there are no records."""
    if not appointments:
        print("There are no appointments available.")
        return None

    while True:
        id_text = input(message).strip()

        try:
            appointment_id = int(id_text)
            appointment = find_appointment_by_id(appointment_id)

            if appointment is not None:
                return appointment_id

            print("That appointment ID was not found.")
        except ValueError:
            print("Please enter the appointment ID as a whole number.")


def get_booking_conflict(doctor_name, appointment_date, appointment_time, ignored_id=None):
    """Check whether an active appointment already uses the same doctor, date and time."""
    for appointment in appointments:
        if ignored_id is not None and appointment["id"] == ignored_id:
            continue

        same_doctor = appointment["doctor_name"].lower() == doctor_name.lower()
        same_date = appointment["date"] == appointment_date
        same_time = appointment["time"] == appointment_time
        active_booking = appointment["status"] != "Cancelled"

        if same_doctor and same_date and same_time and active_booking:
            return appointment

    return None


def add_appointment():
    """Collect appointment details and add a new dictionary to the list."""
    global next_appointment_id

    print("\n--- Add New Appointment ---")

    patient_name = get_valid_name("Enter patient name: ")
    patient_age = get_valid_age()
    doctor_name = get_valid_name("Enter doctor name: ")
    reason = get_non_empty_input("Enter reason for appointment: ")

    while True:
        appointment_date = get_valid_date()
        appointment_time = get_valid_time()

        conflict = get_booking_conflict(
            doctor_name,
            appointment_date,
            appointment_time
        )

        if conflict is None:
            break

        print(
            "That doctor already has an active appointment "
            "at the selected date and time."
        )
        print("Please choose another date or time.")

    appointment = {
        "id": next_appointment_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "doctor_name": doctor_name,
        "reason": reason,
        "date": appointment_date,
        "time": appointment_time,
        "status": "Booked"
    }

    appointments.append(appointment)
    next_appointment_id += 1

    print(f"\nAppointment {appointment['id']} was added successfully.")


def display_one_appointment(appointment):
    """Display one complete appointment record."""
    print("\n----------------------------------------")
    print(f"Appointment ID : {appointment['id']}")
    print(f"Patient Name   : {appointment['patient_name']}")
    print(f"Patient Age    : {appointment['patient_age']}")
    print(f"Doctor         : {appointment['doctor_name']}")
    print(f"Reason         : {appointment['reason']}")
    print(f"Date           : {appointment['date']}")
    print(f"Time           : {appointment['time']}")
    print(f"Status         : {appointment['status']}")


def view_all_appointments():
    """Display every appointment in the current list."""
    print("\n--- All Appointments ---")

    if not appointments:
        print("No appointments have been added yet.")
        return

    for appointment in appointments:
        display_one_appointment(appointment)

    print(f"\nTotal records displayed: {len(appointments)}")


def search_appointments():
    """Search appointment records using a linear search."""
    print("\n--- Search Appointments ---")

    if not appointments:
        print("There are no appointments to search.")
        return

    print("1. Search by patient name")
    print("2. Search by doctor name")
    print("3. Search by date")
    print("4. Search by appointment ID")

    choice = input("Choose a search option: ").strip()
    matches = []

    if choice == "1":
        search_value = get_non_empty_input("Enter patient name: ").lower()

        for appointment in appointments:
            if search_value in appointment["patient_name"].lower():
                matches.append(appointment)

    elif choice == "2":
        search_value = get_non_empty_input("Enter doctor name: ").lower()

        for appointment in appointments:
            if search_value in appointment["doctor_name"].lower():
                matches.append(appointment)

    elif choice == "3":
        search_value = get_valid_date(
            "Enter date to search for (DD/MM/YYYY): ",
            allow_past=True
        )

        for appointment in appointments:
            if appointment["date"] == search_value:
                matches.append(appointment)

    elif choice == "4":
        id_text = input("Enter appointment ID: ").strip()

        try:
            appointment = find_appointment_by_id(int(id_text))

            if appointment is not None:
                matches.append(appointment)
        except ValueError:
            print("Please enter a valid numerical ID.")
            return

    else:
        print("Invalid search option.")
        return

    if matches:
        print(f"\n{len(matches)} matching appointment(s) found:")

        for appointment in matches:
            display_one_appointment(appointment)
    else:
        print("No matching appointment was found.")


def get_sort_value(appointment, sort_choice):
    """Return the value used to compare two appointments."""
    if sort_choice == "1":
        return datetime.strptime(
            appointment["date"] + " " + appointment["time"],
            "%d/%m/%Y %H:%M"
        )

    if sort_choice == "2":
        return appointment["patient_name"].lower()

    if sort_choice == "3":
        return appointment["doctor_name"].lower()

    return appointment["status"].lower()


def bubble_sort_appointments(sort_choice):
    """Return a new list sorted with the bubble sort algorithm."""
    sorted_list = appointments.copy()

    for pass_number in range(len(sorted_list) - 1):
        swapped = False

        for index in range(len(sorted_list) - 1 - pass_number):
            first_value = get_sort_value(sorted_list[index], sort_choice)
            second_value = get_sort_value(sorted_list[index + 1], sort_choice)

            if first_value > second_value:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1],
                    sorted_list[index]
                )
                swapped = True

        if not swapped:
            break

    return sorted_list


def sort_appointments():
    """Let the user choose how to sort and display appointments."""
    print("\n--- Sort Appointments ---")

    if not appointments:
        print("There are no appointments to sort.")
        return

    print("1. Sort by date and time")
    print("2. Sort by patient name")
    print("3. Sort by doctor name")
    print("4. Sort by status")

    choice = input("Choose a sorting option: ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid sorting option.")
        return

    sorted_appointments = bubble_sort_appointments(choice)

    print("\n--- Sorted Appointments ---")
    for appointment in sorted_appointments:
        display_one_appointment(appointment)


def edit_appointment():
    """Edit one field in an existing appointment."""
    print("\n--- Edit Appointment ---")

    if not appointments:
        print("There are no appointments to edit.")
        return

    view_all_appointments()
    appointment_id = get_valid_appointment_id("\nEnter the appointment ID to edit: ")

    if appointment_id is None:
        return

    appointment = find_appointment_by_id(appointment_id)

    print("\n1. Patient name")
    print("2. Patient age")
    print("3. Doctor name")
    print("4. Reason")
    print("5. Date")
    print("6. Time")
    print("0. Cancel editing")

    choice = input("Choose the detail to edit: ").strip()

    if choice == "1":
        appointment["patient_name"] = get_valid_name("Enter new patient name: ")

    elif choice == "2":
        appointment["patient_age"] = get_valid_age()

    elif choice == "3":
        new_doctor = get_valid_name("Enter new doctor name: ")
        conflict = get_booking_conflict(
            new_doctor,
            appointment["date"],
            appointment["time"],
            ignored_id=appointment["id"]
        )

        if conflict is not None:
            print("That doctor is already booked at this date and time.")
            return

        appointment["doctor_name"] = new_doctor

    elif choice == "4":
        appointment["reason"] = get_non_empty_input("Enter new reason: ")

    elif choice == "5":
        new_date = get_valid_date("Enter new date (DD/MM/YYYY): ")
        conflict = get_booking_conflict(
            appointment["doctor_name"],
            new_date,
            appointment["time"],
            ignored_id=appointment["id"]
        )

        if conflict is not None:
            print("That doctor is already booked at this date and time.")
            return

        appointment["date"] = new_date

    elif choice == "6":
        new_time = get_valid_time("Enter new time (HH:MM): ")
        conflict = get_booking_conflict(
            appointment["doctor_name"],
            appointment["date"],
            new_time,
            ignored_id=appointment["id"]
        )

        if conflict is not None:
            print("That doctor is already booked at this date and time.")
            return

        appointment["time"] = new_time

    elif choice == "0":
        print("Editing cancelled.")
        return

    else:
        print("Invalid editing option.")
        return

    print("Appointment details updated successfully.")


def update_status():
    """Update the status of an existing appointment."""
    print("\n--- Update Appointment Status ---")

    if not appointments:
        print("There are no appointments to update.")
        return

    view_all_appointments()
    appointment_id = get_valid_appointment_id(
        "\nEnter the appointment ID to update: "
    )

    if appointment_id is None:
        return

    appointment = find_appointment_by_id(appointment_id)

    print("\n1. Booked")
    print("2. Completed")
    print("3. Cancelled")

    status_choice = input("Choose the new status: ").strip()

    if status_choice == "1":
        conflict = get_booking_conflict(
            appointment["doctor_name"],
            appointment["date"],
            appointment["time"],
            ignored_id=appointment["id"]
        )

        if conflict is not None:
            print("This appointment cannot be rebooked because the time is now occupied.")
            return

        appointment["status"] = "Booked"
    elif status_choice == "2":
        appointment["status"] = "Completed"
    elif status_choice == "3":
        appointment["status"] = "Cancelled"
    else:
        print("Invalid status option.")
        return

    print("Appointment status updated successfully.")


def delete_appointment():
    """Permanently delete an appointment after confirmation."""
    print("\n--- Delete Appointment ---")

    if not appointments:
        print("There are no appointments to delete.")
        return

    view_all_appointments()
    appointment_id = get_valid_appointment_id(
        "\nEnter the appointment ID to delete: "
    )

    if appointment_id is None:
        return

    appointment = find_appointment_by_id(appointment_id)
    display_one_appointment(appointment)

    confirmation = input("\nType Y to confirm deletion: ").strip().lower()

    if confirmation == "y":
        appointments.remove(appointment)
        print("Appointment deleted successfully.")
    else:
        print("Deletion cancelled.")


def save_appointments(show_message=True):
    """Write all appointments to the CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            writer.writerows(appointments)

        if show_message:
            print(f"\nAppointments saved successfully to {os.path.basename(FILE_NAME)}.")

        return True

    except OSError as error:
        print(f"\nThe appointments could not be saved: {error}")
        return False


def load_appointments(show_message=True):
    """Read appointments from the CSV file and replace the current list."""
    global appointments
    global next_appointment_id

    if not os.path.exists(FILE_NAME):
        appointments = []
        next_appointment_id = 1

        if show_message:
            print("\nNo saved appointments file was found. A new file will be created.")

        return False

    loaded_appointments = []
    skipped_rows = 0

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames != FIELD_NAMES:
                raise ValueError("The CSV headings are missing or in the wrong order.")

            for row in reader:
                try:
                    appointment = {
                        "id": int(row["id"]),
                        "patient_name": row["patient_name"].strip(),
                        "patient_age": int(row["patient_age"]),
                        "doctor_name": row["doctor_name"].strip(),
                        "reason": row["reason"].strip(),
                        "date": datetime.strptime(
                            row["date"], "%d/%m/%Y"
                        ).strftime("%d/%m/%Y"),
                        "time": datetime.strptime(
                            row["time"], "%H:%M"
                        ).strftime("%H:%M"),
                        "status": row["status"].strip()
                    }

                    if not appointment["patient_name"] or not appointment["doctor_name"]:
                        raise ValueError("A required text field is empty.")

                    if not 0 <= appointment["patient_age"] <= 120:
                        raise ValueError("Patient age is outside the accepted range.")

                    if appointment["status"] not in VALID_STATUSES:
                        raise ValueError("Appointment status is not valid.")

                    if find_id_in_list(loaded_appointments, appointment["id"]):
                        raise ValueError("A duplicate appointment ID was found.")

                    loaded_appointments.append(appointment)

                except (ValueError, TypeError, KeyError):
                    skipped_rows += 1

        appointments = loaded_appointments
        next_appointment_id = max(
            [appointment["id"] for appointment in appointments],
            default=0
        ) + 1

        if show_message:
            print(f"\n{len(appointments)} appointment(s) loaded successfully.")

            if skipped_rows > 0:
                print(f"{skipped_rows} invalid row(s) were safely skipped.")

        return True

    except (OSError, ValueError) as error:
        print(f"\nThe appointments file could not be loaded: {error}")
        return False


def find_id_in_list(appointment_list, appointment_id):
    """Return True when an ID is already present in a supplied list."""
    for appointment in appointment_list:
        if appointment["id"] == appointment_id:
            return True

    return False


def count_appointments_recursively(index=0):
    """Count the appointment list using recursion."""
    if index >= len(appointments):
        return 0

    return 1 + count_appointments_recursively(index + 1)


def count_status(status_name):
    """Count appointments with a particular status."""
    count = 0

    for appointment in appointments:
        if appointment["status"] == status_name:
            count += 1

    return count


def show_bar(label, amount):
    """Display a simple text-based data visualisation."""
    bar = "#" * amount
    print(f"{label:<10} | {bar} ({amount})")


def show_summary():
    """Display totals and a text chart of appointment statuses."""
    print("\n--- Appointment Summary ---")

    total = count_appointments_recursively()
    booked = count_status("Booked")
    completed = count_status("Completed")
    cancelled = count_status("Cancelled")

    print(f"Total appointments: {total}")
    print("\nStatus Chart")
    show_bar("Booked", booked)
    show_bar("Completed", completed)
    show_bar("Cancelled", cancelled)

    if total == 0:
        print("\nNo appointment data is currently available.")


def main():
    """Run the program until the user chooses to exit."""
    load_appointments(show_message=False)

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
            edit_appointment()
            pause_program()
        elif choice == "6":
            update_status()
            pause_program()
        elif choice == "7":
            delete_appointment()
            pause_program()
        elif choice == "8":
            save_appointments()
            pause_program()
        elif choice == "9":
            load_appointments()
            pause_program()
        elif choice == "10":
            show_summary()
            pause_program()
        elif choice == "0":
            if save_appointments(show_message=False):
                print("\nAppointments saved.")
            print("Thank you for using the Clinic Appointment Management System.")
            break
        else:
            print("Invalid choice. Please select an option shown in the menu.")
            pause_program()


if __name__ == "__main__":
    main()
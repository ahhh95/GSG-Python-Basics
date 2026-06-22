import json
import random

patients = []


# Load data from file
def load_data():
    global patients
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        patients = []
        print("No saved data found. Starting with an empty system.")


# Save data to file
def save_data():
    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)
    print("Data saved successfully.")


# Show menu
def show_menu():
    print("\n====== Clinic Patient Management System ======")
    print("1. Add New Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient Information")
    print("5. Add Visit Note")
    print("6. View Patient History")
    print("7. Save Data")
    print("8. Exit")


# Add patient
def add_patient():
    name = input("Enter patient name: ").strip().title()

    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    phone = input("Enter phone number: ").strip()
    symptoms = input("Enter symptoms: ").strip()

    patient_id = random.randint(1000, 9999)

    while any(patient["id"] == patient_id for patient in patients):
        patient_id = random.randint(1000, 9999)

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "phone": phone,
        "symptoms": symptoms,
        "visits": []
    }

    patients.append(patient)
    print("Patient added successfully.")


# View all patients
def view_patients():
    if len(patients) == 0:
        print("No patients found.")
    else:
        print("\n====== All Patients ======")

        for patient in patients:
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Phone:", patient["phone"])
            print("Symptoms:", patient["symptoms"])
            print("-------------------------")


# Search patient
def search_patient():
    search = input("Enter patient name or ID: ").strip()

    found = False

    for patient in patients:
        if search.lower() in patient["name"].lower() or search == str(patient["id"]):
            print("\nPatient found:")
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Phone:", patient["phone"])
            print("Symptoms:", patient["symptoms"])
            found = True

    if not found:
        print("Patient not found.")


# Update patient information
def update_patient():
    patient_id = input("Enter patient ID to update: ")

    for patient in patients:
        if str(patient["id"]) == patient_id:

            print("1. Name")
            print("2. Age")
            print("3. Phone")
            print("4. Symptoms")

            choice = input("Choose an option: ")

            if choice == "1":
                patient["name"] = input("Enter new name: ").title()

            elif choice == "2":
                try:
                    patient["age"] = int(input("Enter new age: "))
                except ValueError:
                    print("Invalid age.")
                    return

            elif choice == "3":
                patient["phone"] = input("Enter new phone number: ")

            elif choice == "4":
                patient["symptoms"] = input("Enter new symptoms: ")

            else:
                print("Invalid choice.")
                return

            print("Patient updated successfully.")
            return

    print("Patient not found.")


# Add visit note
def add_visit_note():
    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if str(patient["id"]) == patient_id:

            date = input("Enter visit date: ")
            doctor = input("Enter doctor name: ")
            note = input("Enter visit note: ")
            advice = input("Enter prescription or advice: ")

            visit = {
                "date": date,
                "doctor": doctor,
                "note": note,
                "advice": advice
            }

            patient["visits"].append(visit)

            print("Visit note added successfully.")
            return

    print("Patient not found.")


# View patient history
def view_patient_history():
    patient_id = input("Enter patient ID: ")

    for patient in patients:
        if str(patient["id"]) == patient_id:

            print("\nPatient:", patient["name"])

            if len(patient["visits"]) == 0:
                print("No visit history.")
            else:
                count = 1

                for visit in patient["visits"]:
                    print("\nVisit", count)
                    print("Date:", visit["date"])
                    print("Doctor:", visit["doctor"])
                    print("Note:", visit["note"])
                    print("Advice:", visit["advice"])
                    count += 1

            return

    print("Patient not found.")


# Main program
def main():
    load_data()

    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            add_visit_note()

        elif choice == "6":
            view_patient_history()

        elif choice == "7":
            save_data()

        elif choice == "8":
            answer = input("Do you want to save before exiting? (yes/no): ").lower()

            if answer == "yes":
                save_data()

            print("Thank you for using the Clinic Patient Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
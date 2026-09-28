 # MODULE WHICH ARE USE TO CREAT THIS PROJECT
import json
from datetime import datetime
import random
import string

# THIS IS THE FILE NAME WHERE THE PATIENT HISTORY SAVED
FILE_NAME = "patients.json"

# LOADING PATIENT DATA FROM patient.json FILE
def load_patients():
    try:      # USE try-except TO HANDL ERROR IF THE patient.jason FILE IS NOT SAVE
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}

# FOR SAVING PATIENT DATA IN patient.json FILE
def save_patients(patients):
    with open(FILE_NAME,"w") as file:
        json.dump(patients, file, indent=4)

# FOR RECEPTIONIST LOGIN 
def receptionist_login():
    print("<<<<<<--------RECEPTIONIST LOGIN-------->>>>>>")
    username = input("Enter username--->").upper().replace(" ","")
    password = input("Enter password--->").replace(" ","")
    
    # CREATING CAPTCHA FOR MAXIMUM SECURITY
    character = string.digits
    Captcha = ''.join(random.choice(character) for _ in range(6))   
    print("CAPTCHA",Captcha)
    Enter_Captcha = input("Enter captcha--->")
    
    # TO VERIFY USERNAME,CAPTCHA,PASSWORD 
    if username == "RECEPTIONIST" and password == "receptionist123" and Enter_Captcha == Captcha:
        print("\nReceptionist login successfuul.\nWELCOME RECEPTIONIST")
        receptionist_menu()
    else:
        print("\nInvalid credential!")

# FOR DOCTOR LOGIN
def doctor_login():
    print("<<<<<<--------DOCTOR LOGIN-------->>>>>>")
    username = input("Enter username--->").upper().replace(" ","")
    password = input("Enter password--->").replace(" ","")
    
    # CREATING CAPTCHA FOR MAXIMUM SECURITY
    character = string.digits
    Captcha = ''.join(random.choice(character) for _ in range(6))   
    print("CAPTCHA",Captcha)
    Enter_Captcha = input("Enter captcha--->")
   
    # TO VERIFY USERNAME,CAPTCHA,PASSWORD 
    if username == "DOCTOR" and password == "doctor123" and Enter_Captcha == Captcha:
        print("\nDoctor login successful!")
        doctor_menu()
    else:
        print("\nInvalid credential!")

# FOR PATIENT LOGIN
def patient_login():
    print("<<<<<<--------PATIENT LOGIN-------->>>>>>")

    patient_id = input("Enter Patient ID---> ").replace(" ","")
    patients = load_patients()
    if patient_id not in patients:
        print("\nPatient ID not found!")
        return
    password = input("Enter password--->").replace(" ","")
     # CREATING CAPTCHA FOR MAXIMUM SECURITY
    character = string.digits
    Captcha = ''.join(random.choice(character) for _ in range(6))   
    print("CAPTCHA",Captcha)
    Enter_Captcha = input("Enter captcha--->")
        # TO VERIFY USERNAME,CAPTCHA,PASSWORD 
    if password == patients[patient_id]["password"] and Enter_Captcha == Captcha:
        print("\nPatient login successful!")
        patient_menu(patient_id)
    else:
        print("\nInvalid credential!")

# RECEPTIONIST'S FEATURES 
def receptionist_menu():
    while True:
        print("\n<<<<<<-------RECEPTIONIST MENU-------->>>>>>")
        print("1. Add Patient")
        print("2. Update Patient Details")
        print("3. View All Patients")
        print("4. Search patient")
        print("5. Delete patient")
        print("6. Logout")
        print("\n HELLO RECEPTIONIST\nHow i help you?")
        option = input("Enter your choice(1-6): ")
        if option == "1":
            add_patient()
        elif option == "2":
            update_patient_details()
        elif option == "3":
            view_all_patients()
        elif option == "4":
            search_patient()
        elif option == "5":
            delete_patient()
        elif option == "6":
            print("\nLogged out successfully!")
            break
        else:
            print("\nInvalid choice!")

# FOR ADD & STORE PATIENT DETAILS 
def add_patient():
    patients = load_patients()
    print("\n<<<<<<--------ADD PATIENT-------->>>>>>")
    patient_id = input("Enter Patient ID--->")
    if patient_id in patients:
        print("\nThis Patient ID already exists!\nPlease try a new one")
        return

    name = input("Enter patient name--->")
    age = input("Enter age--->")
    gender = input("Enter gender--->")
    disease = input("Enter disease--->")
    address = input("Enter address--->")
    mobile_no =input("Enter mobile no--->")
    password = mobile_no
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "address": address,
        "mobile_no": mobile_no,
        "date": current_datetime,
        "password": password,
        "treatment": []
    }
    save_patients(patients)
    print("\nPatient added successfully!")
    print("Patient ID:", patient_id)
    print("Date & Time:", current_datetime)

#FOR UPDATE PATIENT DETAILS
def update_patient_details():
    patients = load_patients()
    print("\n--------UPDATE PATIENT DETAILS--------")
    patient_id = input("Enter Patient ID--->")
    if patient_id not in patients:
        print("\nPatient not found!")
        return
    patient = patients[patient_id]
    print("\nCurrent Patient Details")
    print("-----------------------------")
    print("Name    :", patient["name"])
    print("Age     :", patient["age"])
    print("Gender  :", patient["gender"])
    print("Address :", patient["address"])
    print("Mobile No :", patient["mobile_no"])
    print("\nLeave the field blank if you do not want to change it.")
    # UPDATE NAME
    new_name = input("Enter updated name--->")
    if new_name != "":
        patient["name"] = new_name
    # UPDATE AGE
    new_age = input("Enter updated age--->")
    if new_age != "":
        patient["age"] = new_age
    # UPDATE GENDER
    new_gender = input("Enter updated gender--->")
    if new_gender != "":
        patient["gender"] = new_gender
    new_mobile = input("Enter updated mobile no--->")
    if new_mobile != "":
        patient["mobile_no"] = new_mobile
    # UPDATE ADDRESS
    new_address = input("Enter updated address--->")
    if new_address != "":
        patient["address"] = new_address
    save_patients(patients)
    print("\nPatient details updated successfully!")

#TO VIEW ALL PATIENT 
def view_all_patients():
    patients = load_patients()
    print("\n<<<<<<--------ALL PATIENTS-------->>>>>>")
    if len(patients) == 0:
        print("No patients found.")
        return
    for patient_id, patient in patients.items():
        print("\n-----------------------------")
        print("Patient ID :", patient_id)
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Gender     :", patient["gender"])
        print("Disease    :", patient["disease"])
        print("Address    :", patient["address"])
        print("Mobile No  :", patient["mobile_no"])
        print("Registered :", patient["date"])

        if len(patient["treatment"]) > 0:
            print("Treatments :")
            for treatment in patient["treatment"]:
                print("  -", treatment)
        else:
            print("Treatments : No treatment added")

#DOCTOR'S FEATURE
def doctor_menu():
    while True:
        print("\n<<<<<<--------DOCTOR MENU-------->>>>>>")
        print("1. View Patient")
        print("2. Add Treatment")
        print("3. Logout")
        option = input("Enter your choice(1,3): ")
        if option == "1":
            search_patient()
        elif option == "2":
            add_treatment()
        elif option == "3":
            print("\nDoctor logged out.")
            break
        else:
            print("\nInvalid choice!")

#SEARCH PATIENT
def search_patient():
    patients = load_patients()
    print("\n<<<<<<--------SEARCH PATIENT-------->>>>>>")
    patient_id = input("Enter Patient ID--->").replace(" ","")
    if patient_id not in patients:
        print("\nPatient not found!")
        return
    patient = patients[patient_id]
    print("\nPatient Information")
    print("-----------------------------")
    print("Patient ID :", patient_id)
    print("Name       :", patient["name"])
    print("Age        :", patient["age"])
    print("Gender     :", patient["gender"])
    print("Disease     :", patient["disease"])
    print("Address    :", patient["address"])
    print("Mobile No :", patient["mobile_no"])
    print("Registered :", patient["date"])
    print("\nTreatment History:")

    if len(patient["treatment"]) == 0:
        print("No treatment available.")
    else:
        for treatment in patient["treatment"]:
            print("-", treatment)

# ADD TREATMENT BY DOCTOR
def add_treatment():
    patients = load_patients()
    print("\n<<<<<<--------ADD TREATMENT-------->>>>")
    patient_id = input("Enter Patient ID--->")
    if patient_id not in patients:
        print("\nPatient not found!")
        return
    print("\nPatient Name:", patients[patient_id]["name"])
    treatment = input("Enter treatment: ")
    signature = input("Enter your signature--->")
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    treatment_record = current_datetime + " - " + treatment 
    signature = current_datetime + " - " +  signature 
    patients[patient_id]["treatment"].append(treatment_record)
    patients[patient_id]["treatment"].append(signature)
    save_patients(patients)
    print("\nTreatment added successfully!")

# PATIENT'S FEATURE
def patient_menu(patient_id):
    while True:
        print("\n--------PATIENT MENU--------")
        print("1. View My Details")
        print("2. View My Treatment")
        print("3. Logout")
        option = input("Enter your choice(1,3): ")
        if option == "1":
            view_patient_details(patient_id)
        elif option == "2":
            view_my_treatment(patient_id)
        elif option == "3":
            print("\nPatient logged out.")
            break
        else:
            print("\nInvalid choice!")

#VIEW PATIENT DETAILS BY HIM/HER SELF
def view_patient_details(patient_id):
    patients = load_patients()
    patient = patients[patient_id]
    print("\n--------MY DETAILS--------")
    print("Patient ID :", patient_id)
    print("Name       :", patient["name"])
    print("Age        :", patient["age"])
    print("Gender     :", patient["gender"])
    print("Disease     :", patient["disease"])
    print("Address    :", patient["address"])
    print("Mobile No :", patient["mobile_no"])
    print("Registered :", patient["date"])

# VIEW TREATMENT HISTORY BY PATIENT
def view_my_treatment(patient_id):
    patients = load_patients()
    patient = patients[patient_id]
    print("\n--------MY TREATMENT--------")
    if len(patient["treatment"]) == 0:

        print("No treatment has been added yet.")
    else:
        for treatment in patient["treatment"]:
            print("-", treatment)

#TO DELETE PATIENT FROM DATABASE BY RECEPTIONIST
def delete_patient():
    patients = load_patients()
    print("\n--------DELETE PATIENT--------")
    patient_id = input("Enter Patient ID--->")
    if patient_id not in patients:
        print("\nPatient not found!")
        return
    patient = patients[patient_id]
    print("\nPatient Information")
    print("-----------------------------")
    print("Patient ID :", patient_id)
    print("Name       :", patient["name"])
    confirm = input("\nAre you sure? you want to delete this patient. (yes/no): ")

    if confirm.lower() == "yes":
        del patients[patient_id]
        save_patients(patients)
        print("\nPatient deleted successfully!")
    else:
        print("\nDelete operation cancelled!")

#MAIN PROGRAMME
def main():
    while True:
        print("\n")
        print("----------------------------------------------")
        print("      SMALL CLINIC MANAGEMENT SYSTEM")
        print("----------------------------------------------")
        print("1. Receptionist Login")
        print("2. Doctor Login")
        print("3. Patient Login")
        print("4. Exit")
        option = input("\nEnter your choice(1,4)--->")
        if option == "1":
            receptionist_login()
        elif option == "2":
            doctor_login()
        elif option == "3":
            patient_login()
        elif option == "4":
            print("\nThank for using our Clinic Management System.")
            break
        else:
            print("\nInvalid choice! Please try again.")

main()
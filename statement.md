# Problem Statement

Small clinics and local healthcare centres often manage patient records manually using paper registers or basic spreadsheets. This approach leads to several problems:

- Difficulty in quickly retrieving patient history
- Risk of data loss or duplication
- Lack of role-based access control
- No structured way to record and track treatments
- Time-consuming search and update operations

There is a need for a simple, lightweight, and secure digital system that allows clinic staff (Receptionist and Doctor) and patients to manage and view medical records efficiently without requiring complex infrastructure or expensive software.

# Scope of the Project
**In Scope:**
- Role-based login for Receptionist, Doctor, and Patient
- CAPTCHA-based authentication for improved security
- Complete patient lifecycle management (Add, View, Update, Search, Delete)
- Treatment recording by doctors with timestamps and signatures
- Patient self-service view of personal details and treatment history
- Persistent storage of all data in a local JSON file
- Menu-driven user interface

**Out of Scope:**
- Graphical User Interface (GUI)
- Multi-user concurrent access / networking
- Appointment scheduling
- Billing / payment module
- Integration with external hospital systems or databases 
- Mobile application or web deployment
- Advanced analytics or reporting dashboards

# Target Users

1. **Receptionist** – Registers new patients, updates demographic details, searches and manages the patient database.
2. **Doctor** – Views patient information and adds treatment notes / prescriptions with a digital signature.
3. **Patient** – Logs in using their Patient ID to view personal details and treatment history.

# High-Level Features

| Feature                        | Description                                              |  
|--------------------------------|----------------------------------------------------------|
| Secure Login + CAPTCHA         | Role-based authentication with auto generated CAPTCHA           |
| Add Patient                    | Register new patient with timestamp which is generated auto metically              |
| Update Patient Details         | Modify patient's every details                |
| View All Patients              | List complete patient records with treatments            |
| Search Patient                 | View patient details by Patient ID                    |
| Delete Patient                 | Remove patient record with confirmation                  |
| Add Treatment                  | Record treatment + signature + timestamp                 |
| View Own Treatment History     | Patient views all recorded treatments                    |  
| Data  store in             | All records stored in `patients.json`                    |  
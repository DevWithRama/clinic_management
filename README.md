# Small Clinic Management System

## Overview

A console-based **Small Clinic Management System** built in Python. The application manages patient records, treatments, and role-based access for Receptionist, Doctor, and Patient users. All data is stored persistently in a local JSON file (`patients.json`).

The system supports secure login with CAPTCHA, full CRUD operations on patient records, treatment history management by doctors, and self-service views for patients.

## Features

### Receptionist Module
- Secure login (username + password + CAPTCHA)
- Add new patient (auto-generates registration timestamp; password defaults to mobile number)
- Update patient details (name, age, gender, mobile, address)
- View all patients with treatment history
- Search patient by ID
- Delete patient (with confirmation)

### Doctor Module
- Secure login (username + password + CAPTCHA)
- Search / view patient details and treatment history
- Add treatment notes with digital signature and timestamp

### Patient Module
- Secure login using Patient ID + password + CAPTCHA
- View own personal details
- View own treatment history

### Common
- Data persistence using JSON
- CAPTCHA-based authentication for all roles
- Timestamped records for registration and treatments
- Simple menu-driven console interface

## Technologies / Tools Used

- **Language:** Python 3
- **Libraries:** `json`, `datetime`, `random`, `string` (standard library only)
- **Storage:** Local JSON file (`patients.json`)
- **Version Control:** Git / GitHub

## Project Structure

```
Clinic-Management-System/
│
├── Clinic.py              # Main application source code
├── patients.json          # Patient data store (created at runtime)
├── README.md              # This file
├── statement.md           # Problem statement & scope
└── docs/                  # Optional diagrams & screenshots
```

## Steps to Install & Run

### Prerequisites
- Python 3.6 or higher installed on your system

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd Clinic-Management-System
   ```

2. No external packages are required (uses only Python standard library).

### Running the Application
```bash
python Clinic.py
```
or
```bash
python3 Clinic.py
```

### Default Credentials

| Role          | Username       | Password          |
|---------------|----------------|-------------------|
| Receptionist  | RECEPTIONIST   | receptionist123   |
| Doctor        | DOCTOR         | doctor123         |
| Patient       | (Patient ID)   | (mobile number set at registration) |

> **Note:** CAPTCHA is generated dynamically on every login attempt and must be entered correctly.

## Instructions for Testing

1. **Receptionist Login**
   - Choose option `1`
   - Enter username `RECEPTIONIST`, password `receptionist123`, and the displayed CAPTCHA
   - Test: Add Patient → View All Patients → Search → Update → Delete

2. **Doctor Login**
   - Choose option `2`
   - Enter username `DOCTOR`, password `doctor123`, and CAPTCHA
   - Test: Search an existing patient → Add Treatment (with signature)

3. **Patient Login**
   - Choose option `3`
   - Enter a valid Patient ID (created by receptionist) and the corresponding password (mobile number)
   - Test: View My Details → View My Treatment

4. **Edge Cases**
   - Try invalid credentials / wrong CAPTCHA
   - Search or delete a non-existent Patient ID
   - Leave update fields blank to keep existing values

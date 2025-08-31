# Hospital Management System

A comprehensive hospital management system designed to streamline hospital operations, manage patient information, and facilitate communication between patients and doctors.

## Features

*   **User Authentication:** Secure registration and login for patients, doctors, and hospital administrators.
*   **Appointment Scheduling:** Patients can book appointments with doctors, and doctors can view their upcoming appointments.
*   **Patient Management:** Doctors can view and manage their patients' medical records and history.
*   **Admin Dashboard:** Administrators can manage doctors, patients, and appointments through a centralized dashboard.

## Technologies Used

*   **Backend:** Django, Python
*   **Frontend:** HTML, CSS
*   **Database:** SQLite

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/hospital-management.git
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

*   **Admin:** Access the admin dashboard at `/admin` to manage the system.
*   **Patient:** Register, log in, and book appointments with doctors.
*   **Doctor:** Log in to view appointments and manage patient records.

## Project Structure

```
├── accounts/
├── hospital/
├── hospitals/
├── manage.py
└── README.md
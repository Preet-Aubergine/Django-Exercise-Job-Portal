# Django Job Portal Project

This is a Django-based Job Portal application where users can register, log in, create and manage company details, post jobs, view job listings, and edit/delete job postings. The project uses PostgreSQL as the database, Bootstrap for frontend styling.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- Python (3.8 or above)
- PostgreSQL
- Virtualenv (optional but recommended)

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/job-portal.git
cd job-portal
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install required Python packages
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### PostgreSQL Setup (If applicable):

  - Install PostgreSQL on your machine if not already installed.
  - Create a new PostgreSQL database named companydetail (or modify the settings in your settings.py file).
  - Configure the database connection settings in the settings.py file.

#### Apply Migrations:
```bash
python manage.py migrate
```

#### Create a Superuser (Optional):
```bash
python manage.py createsuperuser
```

### 5. Running the Project
```bash
python manage.py runserver
```

### 6. Key Components
  - portal/: Handles user authentication (register, login, logout).
  - companies/: Manages company details (name, address, contact).
  - jobs/: Allows users to post and manage job listings.

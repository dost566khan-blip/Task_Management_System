# FastAPI Task Management System

A RESTful Task Management API built using **Python and FastAPI**, with user authentication, JWT-based authorization, and PostgreSQL database integration.

## Features

### User Management
- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Authentication Verification
- Duplicate User Validation

### Task Management
- Create Tasks
- Retrieve Tasks
- Update Tasks
- Delete Tasks

### Security
- Password hashing using Passlib
- JWT-based authentication
- Protected API endpoints
- Environment-based configuration

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- PyJWT
- Passlib
- Uvicorn

## Project Structure

```text
Task_management_app/
│
├── src/
│   ├── tasks/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── constent.py
│       ├── db.py
│       ├── helpers.py
│       └── settings.py
│
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dost566khan-blip/Task_Management_System.git
```

### 2. Navigate to the Project

```bash
cd Task_Management_System
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the root directory.

Add your own PostgreSQL database connection and JWT configuration:

```env
DB_CONNECTION=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```

**Important:** Never upload your actual `.env` file or secret credentials to GitHub.

### 7. Run the Application

```bash
fastapi dev main.py
```

## API Documentation

After starting the application, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Database

This project uses PostgreSQL as its relational database and SQLAlchemy for database operations.

## Author

**Dost Muhammad Khan**

GitHub: https://github.com/dost566khan-blip

# Django REST Framework Todo API Engine 🚀

An enterprise-grade, secure, and fully containerized Task Management REST API built with Django and Django REST Framework (DRF). This project emphasizes strict multi-user data isolation, robust Test-Driven Development (TDD), and modern DevOps practices.

---

## 🌟 Key Features

- **Custom Authentication & Profiles:** Extended Custom User Model utilizing `email` as the unique identifier, paired with automated User Profile creation via Django Signals.
- **Robust JWT Security:** Token-based authentication using SimpleJWT (Access/Refresh tokens) with stateless session management.
- **Advanced Data Isolation (Anti-IDOR):** Bulletproof security implemented at the Serializer layer. Dynamic Queryset filtering prevents users from creating, viewing, updating, or deleting tasks belonging to other users' todo lists.
- **100% Passing Test Suite:** Developed using strict TDD principles, containing **35 automated test cases** covering Models, Serializers, Authentication, and complete API Views.
- **Automated Documentation:** Fully compliant OpenAPI 3 schema representation generated via `drf-spectacular`, exposing an interactive Swagger UI.
- **Production-Ready Infrastructure:** Configured to run seamlessly with a **PostgreSQL** database within isolated environments.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Security:** Django SimpleJWT (JSON Web Tokens)
- **Documentation:** OpenAPI 3, Swagger UI (`drf-spectacular`)
- **Containerization:** Docker, Docker Compose

---

## 📦 Directory Structure

The repository maintains a clean, scannable architecture:


```

DJANGO-TODO/
│
├── core/                  # Django Project Root
│   ├── accounts/          # Authentication & User Profiles App
│   ├── todo/              # Task Management App
│   ├── core/              # Main Settings & WSGI Configuration
│   ├── static/            # Static Files Directory
│   └── manage.py
│
├── Dockerfile             # Multi-stage Docker build file
├── docker-compose.yml     # Production orchestration for web and db services
├── requirements.txt       # Hardened dependency tracking
└── schema.yml             # Generated OpenAPI 3 Spec Sheet

```

---

## 🚀 Quick Start & Installation

Thanks to Docker, you can spin up the entire ecosystem (Django web server + PostgreSQL database + Migrations) using a single command.

### Prerequisites
Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Execution Steps
1. Clone the repository and navigate to the project directory.
2. Run the following command in your terminal:

```bash
docker-compose up --build

```

This command will:

* Build the Python environment and install all dependencies.
* Pull and configure the PostgreSQL database container.
* Apply database migrations automatically.
* Start the development server.

---

## 🧪 Running the Test Suite

To execute the full suite of **35 tests** across all applications, run the following command within the main container or locally:

```bash
python manage.py test

```

### Test Coverage Highlights:

* **Accounts (14 tests):** Tests User creation, Superuser logic, Signals, JWT Login, and Profile updates.
* **Todo (21 tests):** Tests Model integrity, Serializer routing switches, Viewsets, and extensive object-level security policies (IDOR checks).

---

## 📑 API Documentation

Once the containers are up and running, you can access the interactive Swagger UI documentation to explore and test the endpoints directly from your browser:

* **Swagger UI:** `http://localhost:8000/api/v1/schema/swagger-ui/`

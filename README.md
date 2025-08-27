# E-commerce Product API  

A **Django REST Framework (DRF)** API for managing products, categories and users in an e-commerce platform.  

This project was built as part of the **ALX Backend Engineering Capstone** to demonstrate the design and implementation of a real-world backend service. It mimics the responsibilities of a backend developer in the e-commerce space: managing product catalogs, handling user authentication, implementing search and filtering and preparing the system for deployment.  A **Django REST Framework (DRF)** API for managing products, categories, and users in an e-commerce platform.  

Built as part of the **ALX Backend Engineering Capstone Project**, this API demonstrates real-world backend development tasks: product management, authentication, search, filtering, and deployment readiness.  

##  Table of Contents  
- [Project Overview](#project-overview)  
- [Functional Requirements](#functional-requirements)  
- [Technical Requirements](#technical-requirements)  
- [System Architecture](#system-architecture)  
- [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)  
- [Project Structure](#project-structure)  
- [Setup Instructions](#setup-instructions)  
- [API Endpoints](#api-endpoints)  
- [Example Requests](#example-requests)  
- [Error Handling](#error-handling)  
- [Current Status](#current-status)  
- [Roadmap / Stretch Goals](#roadmap--stretch-goals)  
- [Deployment](#deployment)  
- [About](#about)  

##  Project Overview  

The **E-commerce Product API** is a backend service designed to power product management features of an e-commerce platform.  

| Area                  | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Core Purpose**       | Backend API for e-commerce product catalog management                      |
| **Frameworks**         | Django 5.2, Django REST Framework, django-filter                           |
| **Database**           | SQLite (development), PostgreSQL (production)                              |
| **Auth**               | Token-based authentication to secure API endpoints(DRF)                                           |
| **Features**           | Products CRUD, Categories CRUD, User Auth, Search, Filtering, Pagination   |
| **Admin**              | Django Admin site for superuser management                                 |


## Functional Requirements  

### Product Management (CRUD)  
- Create, Read, Update, Delete products  
- Product attributes: `Name`, `Description`, `Price`, `Category`, `Stock Quantity`, `Image URL`, `Created Date`.  
- Validations:  
  - Price must be positive  
  - Stock cannot be negative  
- (Future) Stock automatically reduced when an order is placed  

### User Management  
- Register, login and manage profiles  
- Fields: `Username`, `Email`, `Password`, `First Name`, `Last Name` 
- Only authenticated users can manage (create/update/delete) products  

### Product Search & View  
- Search by product `name` or `category`
- Support partial matches for flexible search
- Filter products by category, price range or stock availability
- Paginated product listing for performance


##  Technical Requirements  

| Area          | Details                                                                 |
|---------------|-------------------------------------------------------------------------|
| **Database**  | Django ORM with SQLite (dev) and PostgreSQL (prod)                      |
| **Auth**      | Django built-in user + DRF Token Auth                                   |
| **API Design**| RESTful (GET, POST, PUT, DELETE) with proper HTTP status codes          |
| **Deployment**| Ready for Heroku or PythonAnywhere (production config, static, DB)      |


##  System Architecture  

- **Users App**: Custom user model, registration, login, profile  
- **Categories App**: Category model + CRUD  
- **Products App**: Product model linked to user & category + CRUD, search, filtering.  
- **DRF**: Serializers + ViewSets for endpoints  
- **Authentication**: Token-based (suitable for frontend/mobile clients)  


## Entity Relationship Diagram (ERD)

- One **User** can create many Products.  
- One **Category** can contain many Products.  

- ERD pending 

## Project Structure  
```
ecommerce-product-api/
├── config/                  # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/                # Products app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── admin.py
├── categories/              # Categories app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── admin.py
├── users/                   # Users app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── admin.py
├── requirements.txt
├── requirements.lock
├── README.md
└── manage.py
```

##  Setup Instructions  

```bash
# Clone project
git clone https://github.com/TaiWowAde/E_Commerce_Product_API.git
cd E_Commerce_Product_API

# Virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations & create superuser
python manage.py migrate
python manage.py createsuperuser

# Run server
python manage.py runserver

```
•	API Root: http://127.0.0.1:8000/api/
•	Admin: http://127.0.0.1:8000/admin/


## API Endpoints

## About

Author: Taiwo Adeyinka (@TaiWowAde)
Project: ALX Backend Engineering Capstone — E-commerce Product API


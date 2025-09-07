# E-commerce Product API  

The E-commerce Product API is a backend service developed as part of the ALX Backend Engineering Capstone. It is designed to simulate real-world backend development tasks in the e-commerce space, focusing on product catalog management, user authentication, search and filtering.

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
- [About](#about)  

##  Project Overview  

This project follows RESTful principles and is implemented with Django and Django REST Framework. It provides a secure, modular, and extensible foundation for an e-commerce application, where users can register, log in and manage products and categories. The API supports CRUD operations, token-based authentication and flexible data retrieval with pagination, filtering and search functionality.


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

## API Endpoints

| Endpoint | Method(s) | Description |
|----------|-----------|-------------|
| `/api/products/` | GET | List all products |
| `/api/products/` | POST | Create a new product *(auth required)* |
| `/api/products/{id}/` | GET | Retrieve a single product |
| `/api/products/{id}/` | PUT, PATCH | Update a product *(auth required)* |
| `/api/products/{id}/` | DELETE | Remove a product *(auth required)* |
| `/api/categories/` | GET | List all categories |
| `/api/categories/` | POST | Create a new category *(auth required)* |
| `/api/categories/{id}/` | GET | Retrieve a single category |
| `/api/categories/{id}/` | PUT, PATCH | Update a category *(auth required)* |
| `/api/categories/{id}/` | DELETE | Remove a category *(auth required)* |
| `/api/auth/register/` | POST | Register a new user account |
| `/api/auth/login/` | POST | Obtain an authentication token |
| `/api/users/profile/` | GET | Retrieve the authenticated user's profile |
| `/api/users/profile/` | PUT, PATCH | Update the authenticated user's profile |

## Example Requests

### List Products

**Request**

```bash
curl -X GET http://127.0.0.1:8000/api/products/
```

**Response**

```json
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "description": "Compact wireless mouse",
    "price": "25.99",
    "stock_quantity": 100,
    "image_url": "https://example.com/mouse.jpg",
    "category": 2,
    "created_by": 1,
    "created_date": "2024-01-05T12:00:00Z",
    "updated_date": "2024-01-05T12:00:00Z"
  }
]
```


## About

Author: Taiwo Adeyinka (@TaiWowAde)
Project: ALX Backend Engineering Capstone — E-commerce Product API


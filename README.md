# Travel Booking System

A full-stack **Travel Booking System** built with **Django** (Python) backend and **HTML/CSS/Bootstrap** frontend. The project allows users to search for travel options, make bookings, and view booking history. MySQL is used as the database.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Database Configuration](#database-configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User authentication (Sign Up / Login)
- Search for travel options (by city, date, etc.)
- Book tickets and view booking history
- Admin can add/edit/delete travel options
- Responsive design using Bootstrap
- Backend powered by Django with MySQL database

---

## Technologies

- **Backend:** Django 5.x, Python 3.13
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** MySQL
- **Other Libraries:** mysqlclient, Django ORM

---


---

## Setup & Installation

1. **Clone the repository**

```bash
git clone <repo-link>
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements.txt
CREATE DATABASE travel_db;
python manage.py makemigrations
python manage.py migrate




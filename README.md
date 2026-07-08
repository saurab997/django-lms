# SmartLib - Library Management System

SmartLib is a Django-based web application designed for librarians to manage authors, books, and track real-time book availability inventory. Built as a full CRUD system following Django's Model-View-Template (MVT) architecture and styled with Bootstrap 5.

---

## Features Implemented

### Author Management (Full CRUD)
* Create: Add new authors with browser-native calendar date pickers for birth dates.
* Read: A master layout table list displaying all registered authors and a detailed profile view for each author displaying their complete bibliography.
* Update: Secure forms to modify author names, biographies, or birth details.
* Delete: Removal of author data with an explicit, built-in delete confirmation safety page.

### Book Management (Full CRUD)
* Create: Register new books utilizing automated relation dropdown selectors for authors mapped via Django ForeignKeys.
* Read: A primary inventory table reflecting book titles, assigned authors, unique ISBN values, and real-time stock balances, plus an isolated book detail page compiling specific metrics.
* Update: Data adjustments for tracking inventory quantities (copies_total and copies_available).
* Delete: Removal of cataloged volumes backed by explicit delete confirmation interfaces.

---

## Installation and Local Setup

Follow these steps to spin up the development environment on your local system:

### 1. Clone the Repository

git clone [https://github.com/saurab997/django-lms.git](https://github.com/saurab997/django-lms.git)
cd django-lms

### 2. Set Up a Virtual Environment
python -m venv .venv
# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

3. Install Required Dependencies
pip install -r requirements.txt

4. Apply Database Migrations
python manage.py migrate

5. Launch the Local Development Server
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/authors/ to view the app.

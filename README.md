# SmartLib - Library Management System

SmartLib is a Django-based web application designed for librarians to manage authors, books, and track real-time book availability inventory. Built as a full CRUD system following Django's Model-View-Template (MVT) architecture and styled with Bootstrap 5.

---

## Features Implemented

### Author Management (Full CRUD)

- **Create:** Add new authors with browser-native calendar date pickers for birth dates.
- **Read:** View all registered authors in a master table and access individual author profiles displaying their complete bibliography.
- **Update:** Modify author names, biographies, and birth details.
- **Delete:** Remove author records with a built-in delete confirmation page.

### Book Management (Full CRUD)

- **Create:** Register new books using automated author selection through Django ForeignKey relationships.
- **Read:** View the complete inventory including book titles, authors, ISBNs, and real-time stock balances, along with detailed pages for each book.
- **Update:** Update book information and inventory quantities (`copies_total` and `copies_available`).
- **Delete:** Remove books from the catalog with a delete confirmation page.

---

## Installation and Local Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/saurab997/django-lms.git
cd django-lms
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Launch the Local Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/authors/
```

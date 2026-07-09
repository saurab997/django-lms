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

### Screenshots:
1. Book List
   <img width="1711" height="548" alt="Screenshot 2026-07-09 220450" src="https://github.com/user-attachments/assets/3d575636-824e-4f14-bf78-96d7d459319e" />

2. Book Detail
   <img width="1660" height="918" alt="Screenshot 2026-07-09 220505" src="https://github.com/user-attachments/assets/ae298990-8cc3-419e-b515-c28f6f6967e9" />

3. Add new Book
   <img width="1658" height="898" alt="Screenshot 2026-07-09 220518" src="https://github.com/user-attachments/assets/5a523c44-c416-41ae-9547-086eb961f5ef" />

4. Add new Author
   <img width="1656" height="1011" alt="Screenshot 2026-07-09 220523" src="https://github.com/user-attachments/assets/337b704b-c5d8-4ce7-8ba1-2c0b95fe0aca" />


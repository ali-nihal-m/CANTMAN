# CANTMAN – Canteen Management System

A web-based canteen management system built with Python and Django. CANTMAN provides a simple, user-friendly interface for managing food item inventory, with secure user authentication and full CRUD functionality.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Data Model](#data-model)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Security Notes](#security-notes)
- [Author](#author)
- [License](#license)

---

## Overview

CANTMAN lets users register, log in, and manage canteen food items through a clean web interface. Users can add, view, update, delete, and search food items, and can also delete their own account.

## Features

**Authentication & Account**
- User registration
- Login and logout
- Account deletion

**Food Item Management**
- Add new food items
- View all food items
- Update food item details
- Delete food items
- Search food items

**Navigation**
- Home page with quick access to all modules

## Tech Stack

| Technology  | Purpose              |
|-------------|----------------------|
| Python      | Backend programming  |
| Django      | Web framework        |
| HTML        | Page structure       |
| Bootstrap 5 | Frontend styling     |
| SQLite      | Database             |
| PyCharm     | Development IDE      |

## Data Model

Each food item stores the following fields:

| Field       | Description                  |
|-------------|------------------------------|
| Food Name   | Name of the item             |
| Category    | Category the item belongs to |
| Description | Short description            |
| Price       | Unit price                   |
| Quantity    | Available stock              |

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ali-nihal-m/CANTMAN.git
cd CANTMAN
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment**

Windows:

```powershell
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure environment variables**

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY='your-new-secret-key'
```

Generate a fresh secret key for your local setup:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**6. Apply database migrations**

```bash
python manage.py migrate
```

**7. Run the development server**

```bash
python manage.py runserver
```

Open your browser and visit: <http://127.0.0.1:8000/>

## Usage

1. Register a new account and log in.
2. From the home page, add food items with name, category, description, price, and quantity.
3. View the full list, search by name, and edit or delete entries as needed.
4. Log out when finished, or delete your account from the account options.

## Security Notes

- Never commit your `.env` file. Add it to `.gitignore`.
- Use a unique, freshly generated `DJANGO_SECRET_KEY` for every environment.
- This project is intended for local/academic use. Set `DEBUG = False` and configure `ALLOWED_HOSTS` before any real deployment.

## Author

**Ali Nihal**
GitHub: [@ali-nihal-m](https://github.com/ali-nihal-m)

## License

This project is developed for academic purposes.

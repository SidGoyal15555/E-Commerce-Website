# ShopLite — E-Commerce Product Listing

A local full-stack product catalogue built with Python Flask, SQLite, HTML, CSS and JavaScript.

## Features

- Product listing with name, description, price and image
- Individual product details view
- Search by product name or description
- Filter by category
- Flask JSON API
- SQLite relational database with sample data

## Requirements

- Python 3.10+
- pip
- Modern web browser

## Setup and run

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell: `.venv\Scripts\Activate.ps1`  
   Linux/macOS: `source .venv/bin/activate`

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Create and populate the database:

   ```bash
   python seed.py
   ```

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. Open http://127.0.0.1:5000/ in your browser.

## Database

- Database file: `instance/ecommerce.db` (created automatically)
- Schema: `schema.sql`
- Initialization and sample records: `seed.py`
- Database access: Python `sqlite3` in `db.py`

## Architecture

The browser runs the HTML/CSS/JavaScript frontend and calls Flask JSON API endpoints using `fetch()`. Flask validates query parameters and queries SQLite through Python's `sqlite3` module. The frontend does not access the database directly.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products` | List all products |
| GET | `/api/products?q=watch` | Search product names/descriptions |
| GET | `/api/products?category=Home` | Filter by category |
| GET | `/api/products/<id>` | Get one product |
| GET | `/api/categories` | List categories |

A missing product returns HTTP 404. An overlong search/category parameter returns HTTP 400.

## Author

- Name: [Siddhartha Goyal]

## Scope

This repository implements (product listing website) only. Cart, authentication, authorization, migrations, logging and monitoring are future-stage features.

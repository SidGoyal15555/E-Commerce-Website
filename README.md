# ShopLite — E-Commerce Product Listing (Part 1)

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

Keep the terminal open while using the site. 
Stop the server with `Ctrl+C`.

## Database

- Database file: `instance/ecommerce.db`
- Schema: `schema.sql`
- Initialization and sample records: `seed.py`
- Database access: Python `sqlite3` in `db.py`

## Architecture

The browser runs the HTML/CSS/JavaScript frontend and calls Flask JSON API endpoints using `fetch()`. 
Flask validates query parameters and queries SQLite through Python's `sqlite3` module. 
The frontend does not access the database directly.

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/products` | List all products |
| GET | `/api/products?q=watch` | Search product names/descriptions |
| GET | `/api/products?category=Home` | Filter by category |
| GET | `/api/products/<id>` | Get one product |
| GET | `/api/categories` | List categories |

A missing product returns HTTP 404. An overlong search/category parameter returns HTTP 400.

## Screenshots

- `product_listing.png`

![Product Listing](screenshots/product-listing.png)

- `product_details.png`

![Product Listing](screenshots/product-details.png)

- `product_search_filter.png` (recommended)

![Product Search Filter](screenshots/Product_Search_Filter.png)

- `api_products.png` (recommended)

![Product API Response](screenshots/api_response.png)

- `database_products.png` (recommended)

![Database Products](screenshots/Database_Records.png)

## Git setup

```bash
git init
git add .
git commit -m "Build Flask and SQLite product listing application"
```

Add your remote repository URL and push:

```bash
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## Author

- Name: [Siddhartha Goyal]
- Roll number: [2026PIS55445]

## Scope

This repository implements Part 1 (product listing website) for our Programming Lab Assignment. Cart, authentication, authorization, migrations, logging and monitoring are future-stage features.

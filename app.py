from flask import Flask, jsonify, render_template, request
from db import get_connection, get_product_by_id, initialize_database

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/products/<int:product_id>")
def product_page(product_id):
    return render_template("product.html", product_id=product_id)


@app.get("/api/products")
def list_products():
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()

    if len(query) > 100 or len(category) > 60:
        return jsonify({"error": "Search query or category is too long."}), 400

    sql = """
        SELECT id, name, description, price, image_url, category, created_at
        FROM products
        WHERE 1 = 1
    """
    parameters = []

    if query:
        sql += " AND (name LIKE ? OR description LIKE ?)"
        wildcard = f"%{query}%"
        parameters.extend([wildcard, wildcard])

    if category:
        sql += " AND category = ?"
        parameters.append(category)

    sql += " ORDER BY id"

    with get_connection() as connection:
        rows = connection.execute(sql, parameters).fetchall()

    return jsonify({
        "count": len(rows),
        "products": [dict(row) for row in rows],
    }), 200


@app.get("/api/products/<int:product_id>")
def product_detail(product_id):
    if product_id <= 0:
        return jsonify({"error": "Product ID must be positive."}), 400

    product = get_product_by_id(product_id)
    if product is None:
        return jsonify({"error": "Product not found."}), 404

    return jsonify(product), 200


@app.get("/api/categories")
def list_categories():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT DISTINCT category FROM products ORDER BY category"
        ).fetchall()

    return jsonify([row["category"] for row in rows]), 200


@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "API endpoint not found."}), 404
    return "Page not found", 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error."}), 500


if __name__ == "__main__":
    initialize_database()
    app.run(host="127.0.0.1", port=5000, debug=True)

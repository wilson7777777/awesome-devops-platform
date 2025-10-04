import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Get pod name from environment
POD_NAME = os.environ.get('HOSTNAME', 'unknown-pod')

# Sample in-memory product data
products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "price": 800},
    {"id": 3, "name": "Headphones", "price": 150},
]

# Helper function to include pod info in responses
def with_pod_info(data):
    if isinstance(data, dict):
        data['pod'] = POD_NAME
    elif isinstance(data, list):
        data = [{"pod": POD_NAME, **item} for item in data]
    return data

# Root route
@app.route('/')
def home():
    return jsonify({"message": f"Catalog service is running", "pod": POD_NAME})

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(with_pod_info(products))

# Get a single product by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(with_pod_info(product))
    return jsonify({"error": "Product not found", "pod": POD_NAME}), 404

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({"error": "Invalid request", "pod": POD_NAME}), 400
    new_product = request.json
    new_product['id'] = max((p['id'] for p in products), default=0) + 1
    products.append(new_product)
    return jsonify(with_pod_info(new_product)), 201

# Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found", "pod": POD_NAME}), 404
    data = request.json
    product.update({k: v for k, v in data.items() if k in ["name", "price"]})
    return jsonify(with_pod_info(product))

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found", "pod": POD_NAME}), 404
    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Product deleted", "pod": POD_NAME})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

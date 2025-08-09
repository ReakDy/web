# Import the Flask module and other necessary components
from flask import Flask, request, jsonify
from flask_cors import CORS # Import CORS for cross-origin requests
# Create a Flask application instance
app = Flask(__name__)
# Enable CORS for all routes. This is crucial for allowing your frontend (running on a different origin/port)
# to make requests to this backend. In a production environment, you'd want to restrict this to specific origins.
CORS(app)

# --- Define API Endpoints ---

@app.route('/')
def home():
    """
    A simple home endpoint to confirm the server is running.
    Access this by navigating to http://127.0.0.1:5000/ in your browser.
    """
    return "MiNi 7 Market Backend is Running!"

@app.route('/buy', methods=['POST'])
def buy_product():
    """
    This endpoint simulates a product purchase.
    It expects a JSON payload with 'productName' and 'price'.
    """
    # Check if the request body is JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json() # Get the JSON data from the request body

    product_name = data.get('productName')
    price = data.get('price')

    # Basic validation
    if not product_name or not price:
        return jsonify({"error": "Missing productName or price"}), 400

    # --- Backend Logic (Simulated) ---
    # In a real application, you would:
    # 1. Validate the product and price against a database.
    # 2. Process the payment (integrate with a payment gateway like Stripe, PayPal, etc.).
    # 3. Update inventory.
    # 4. Log the order in a database.
    # 5. Send confirmation emails/notifications.

    print(f"Backend received purchase request:")
    print(f"  Product: {product_name}")
    print(f"  Price: ${price}")
    print(f"  Status: Simulating successful purchase...")

    # For this example, we'll just return a success message.
    return jsonify({
        "message": f"Purchase of {product_name} for ${price} simulated successfully!",
        "status": "success",
        "orderId": "ORD" + str(hash(product_name + str(price))) # A dummy order ID
    }), 200 # 200 OK status code

# --- Main execution block ---
if __name__ == '__main__':
    # Run the Flask application
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    # DO NOT use debug=True in a production environment.
    app.run(debug=True)

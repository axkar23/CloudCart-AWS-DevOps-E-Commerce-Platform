from flask import Flask, render_template, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Cloud Laptop",
        "price": 79999,
        "description": "High-performance laptop for developers."
    },
    {
        "id": 2,
        "name": "DevOps Keyboard",
        "price": 3499,
        "description": "Mechanical keyboard for developers."
    },
    {
        "id": 3,
        "name": "AWS Developer Mouse",
        "price": 1999,
        "description": "Wireless mouse designed for productivity."
    },
    {
        "id": 4,
        "name": "CloudCart Backpack",
        "price": 2499,
        "description": "Durable backpack for laptops and accessories."
    }
]


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CloudCart",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
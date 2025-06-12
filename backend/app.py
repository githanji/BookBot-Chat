from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Product, ChatLog
import datetime
from sqlalchemy import func

app = Flask(__name__)
CORS(app)

# Configure DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    return "Welcome to the E-commerce Chatbot API!"

# Product search with case-insensitive and partial match
@app.route("/search", methods=["GET"])
def search_products():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({"response": "Please enter a search query."})

    results = Product.query.filter(func.lower(Product.name).like(f"%{query.lower()}%")).all()

    if not results:
        return jsonify({"response": "No products found."})

    return jsonify([product.to_dict() for product in results])



# Save chat logs
@app.route("/chatlog", methods=["POST"])
def save_chatlog():
    data = request.json
    chat = ChatLog(
        user=data["user"],
        message=data["message"],
        timestamp=datetime.datetime.now()
    )
    db.session.add(chat)
    db.session.commit()
    return jsonify({"message": "Chat saved"})

if __name__ == '__main__':
    app.run(debug=True)

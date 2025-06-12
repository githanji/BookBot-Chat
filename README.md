# 🛍️ E-commerce Chatbot Backend (Flask API)

This is the backend API for the E-commerce Chatbot application built using **Python**, **Flask**, and **SQLite**. It handles product search queries, stores chat logs, and serves data to a React-based chatbot frontend.

---

## 🚀 Features

- REST API to search products (`/search`)
- Chat log saving (`/chatlog`)
- SQLAlchemy ORM with SQLite
- Database seeding with 100+ mock book entries
- CORS-enabled for frontend integration

---

## 📁 Folder Structure

1. backend/

├── app.py # Flask application entry point

├── models.py # SQLAlchemy models (Product, ChatLog)

├── seed.py # Script to seed 100+ books into SQLite DB

├── requirements.txt # Python dependencies

├── data.db # SQLite database (auto-created)

└── README.md # This file



2. Create Virtual Environment

       python -m venv venv
       venv\Scripts\activate  # or `source venv/bin/activate` on Mac/Linux
   
3. Install Dependencies

       pip install -r requirements.txt

4. Seed the Database

      python seed.py
   
  Output : "Database seeded with 100+ books!"

6. Run the Flask App

     python app.py
   
 Running on http://127.0.0.1:5000/



🔌 API Endpoints


🔍 GET /search?q=<query>


Search books by name (case-insensitive, partial match).

Example:

        GET /search?q=code
        
Response:

            [
               {
                   "id": 3,
                   "name": "Clean Code Vol 5",
                    "price": 550,
                   "category": "Programming"
               }
             ]

             
📝 POST /chatlog

Save a user message.

Request Body:

json

          {
             "user": "guest",
             "message": "clean code"
           }
Response:

  json

          { "message": "Chat saved" }
          
🧪 Testing

Use Postman, Insomnia, or a browser for GET requests like:


        http://127.0.0.1:5000/search?q=zero
        
🧰 Tech Stack

   Backend: Python, Flask, SQLAlchemy

   Database: SQLite

  Tools: Flask-CORS, Axios (on frontend), Postman (testing)

🧠 Future Improvements

Add pagination and filtering (by category or price)

Integrate JWT for authentication

Add Swagger/OpenAPI docs for endpoints

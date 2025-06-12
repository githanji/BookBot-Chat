from models import db, Product
from app import app
import random

categories = [
    "Fiction", "Fantasy", "Sci-Fi", "Business", "Programming",
    "Self-Help", "Education", "Spirituality", "Startup", "Productivity"
]

book_titles = [
    "Zero to One", "Rich Dad Poor Dad", "Clean Code", "The Great Gatsby",
    "The Power of Now", "Atomic Habits", "Harry Potter", "The Lean Startup",
    "1984", "Deep Work", "Start With Why", "The Alchemist", "The Pragmatic Programmer",
    "Thinking Fast and Slow", "The 7 Habits of Highly Effective People", "Dune", "Brave New World",
    "To Kill a Mockingbird", "The Subtle Art of Not Giving a F*ck", "Sapiens", "Hooked", "The Design of Everyday Things"
]


mock_books = []

for i in range(1, 101):
    base = random.choice(book_titles)
    category = random.choice(categories)
    price = random.randint(200, 800)
    title = f"{base} Vol {i}"
    mock_books.append(Product(name=title, price=price, category=category))

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all(mock_books)
    db.session.commit()
    print("Database seeded with 100+ books!")

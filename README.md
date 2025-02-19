# Expense-Tracker
A simple Expense Tracker built using Flask, HTML, CSS, and SQLite. This project helps users record and track their daily expenses in an easy-to-use interface

🔹 Features
✅ Add expenses with amount, category, description, and date
✅ View all expenses in a structured table format
✅ Simple and clean UI with CSS styling
✅ Uses SQLite as the database
✅ Built with Flask (lightweight and easy to set up)

 Installation & Setup
pip install flask
python app.py

Project Structure
expense-tracker/
│── app.py              # Main Flask application
│── database.db         # SQLite database (auto-created)
│── static/             # CSS, images, JS (if needed)
│   ├── style.css       # Main CSS file
│── templates/          # HTML files
│   ├── index.html      # Home page (display expenses)
│   ├── add.html        # Form to add expenses

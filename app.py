from flask import Flask
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
    ''')

    cursor.execute("INSERT INTO projects (title) VALUES ('AI Chatbot')")
    conn.commit()
    conn.close()

create_database()

@app.route('/')
def home():
    return "<h1>Portfolio Database Connected Successfully!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
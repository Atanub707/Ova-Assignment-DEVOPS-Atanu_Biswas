from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('chat_history.db')
    c = conn.cursor()
    return conn, c

# Create a new SQLite database table to store chat history
def create_table():
    conn, c = connect_db()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                 (id INTEGER PRIMARY KEY, email TEXT, message TEXT)''')
    conn.commit()
    conn.close()

# Add chat history to the database
def add_to_history(email, message):
    conn, c = connect_db()
    c.execute("INSERT INTO chat_history (email, message) VALUES (?, ?)", (email, message))
    conn.commit()
    conn.close()

# Retrieve chat history for a specific user
def get_chat_history(email):
    conn, c = connect_db()
    c.execute("SELECT * FROM chat_history WHERE email=?", (email,))
    history = c.fetchall()
    conn.close()
    return history

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    email = data.get('email')
    message = data.get('message')

    add_to_history(email, message)

    return jsonify({'message': 'Message sent successfully!'})

@app.route('/get_chat_history', methods=['POST'])
def get_chat():
    data = request.get_json()
    email = data.get('email')

    history = get_chat_history(email)

    return jsonify(history)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)

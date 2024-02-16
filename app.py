import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('ITservice.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/services')
def get_services():
    conn = get_db_connection()
    services = conn.execute('SELECT id, name, description, imageurl FROM services').fetchall()
    conn.close()
    return jsonify([dict(service) for service in services])

if __name__ == '__main__':
    app.run(debug=True)
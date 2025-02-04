from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Database connection
db = mysql.connector.connect(
    host="34.70.123.199",
    user="wixuser",
    password="Emceelit1!",
    database="wix_data"
)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM research WHERE title LIKE %s OR content LIKE %s", (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Runs on port 5000

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB = "app.db"


@app.get("/users/search")
def search_users():
    name = request.args.get("name", "")
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email FROM users WHERE name LIKE '%{name}%'")
    rows = cur.fetchall()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "email": r[2]} for r in rows])

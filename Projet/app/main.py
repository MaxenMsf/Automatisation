from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE_PATH = 'database.db'

def execute_query(query):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        
        if query.strip().upper().startswith('SELECT'):
            # Pour les requêtes SELECT, récupérer les résultats
            columns = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            result = [dict(zip(columns, row)) for row in rows]
        else:
            # Pour les autres requêtes (INSERT, UPDATE, DELETE)
            conn.commit()
            result = {"affected_rows": cursor.rowcount}
        
        conn.close()
        return {"success": True, "data": result}
    
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/query', methods=['POST'])
def query_database():
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({"success": False, "error": "Missing 'query' parameter"}), 400
        
        query = data['query']
        result = execute_query(query)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 400
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
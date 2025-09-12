from flask import Flask, request, jsonify
from processing_scripts import DataProcessor
import os

app = Flask(__name__)

# URL du service de données (peut être configurée via variable d'environnement)
DATA_SERVICE_URL = os.getenv('DATA_SERVICE_URL', 'http://localhost:5001')
processor = DataProcessor(DATA_SERVICE_URL)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "processing-service"}), 200

@app.route('/users/all', methods=['GET'])
def get_all_users():
    """Endpoint pour récupérer tous les utilisateurs"""
    result = processor.get_all_users()
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/users/count', methods=['GET'])
def count_users():
    """Endpoint pour compter les utilisateurs"""
    result = processor.count_users()
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/users/domain/<domain>', methods=['GET'])
def get_users_by_domain(domain):
    """Endpoint pour récupérer les utilisateurs par domaine"""
    result = processor.get_users_by_domain(domain)
    if result.get("success"):
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@app.route('/process', methods=['POST'])
def custom_process():
    """Endpoint pour exécuter une requête personnalisée"""
    try:
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({"success": False, "error": "Missing 'query' parameter"}), 400
        
        query = data['query']
        result = processor.send_query(query)
        return jsonify(result), 200 if result.get("success") else 400
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
#!/bin/sh

echo "🔍 Vérification des services..."

# Fonction pour tester un endpoint
test_endpoint() {
    local url=$1
    local name=$2
    
    echo "Testing $name ($url)..."
    if curl -s -f "$url" > /dev/null; then
        echo "✅ $name: OK"
        return 0
    else
        echo "❌ $name: ÉCHEC"
        return 1
    fi
}

# Attendre que les services soient prêts
echo "⏳ Attente du démarrage des services..."
sleep 10

# Tester les endpoints
test_endpoint "http://localhost:5001" "Service de données"
test_endpoint "http://localhost:5001/health" "Health check données"
test_endpoint "http://localhost:5002" "Service de traitement"
test_endpoint "http://localhost:5002/health" "Health check traitement"

# Tester la communication entre services
echo ""
echo "🔗 Test de communication entre services..."
curl -s -X POST http://localhost:5002/process \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT name FROM sqlite_master WHERE type='\''table'\''"}' \
  | jq '.' 2>/dev/null || echo "Test de requête SQL effectué"

echo ""
echo "📋 État des pods et conteneurs:"
podman pod ps
echo ""
podman ps -a

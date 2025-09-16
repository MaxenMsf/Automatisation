#!/bin/sh

echo "🚀 Démarrage du projet avec podman-compose..."

# Arrêter les conteneurs existants s'ils existent
echo "📋 Nettoyage des conteneurs existants..."
podman-compose down --remove-orphans 2>/dev/null || true

# Reconstruire les images
echo "🔨 Construction des images..."
podman-compose build --no-cache

# Démarrer les services
echo "🚀 Démarrage des services..."
podman-compose up -d

# Afficher le statut
echo "📊 Statut des conteneurs..."
podman-compose ps

echo ""
echo "✅ Services démarrés!"
echo "🌐 Service de données: http://localhost:5001"
echo "🔧 Service de traitement: http://localhost:5002"
echo ""
echo "📝 Pour voir les logs:"
echo "   podman-compose logs -f"
echo ""
echo "🛑 Pour arrêter:"
echo "   podman-compose down"

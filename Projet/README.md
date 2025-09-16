# Projet de Services Conteneurisés avec Podman

Ce projet illustre l'utilisation de pods Podman pour orchestrer deux services Flask qui communiquent entre eux.

## Architecture

- **Service de données** (port 5001) : API pour exécuter des requêtes SQL sur une base SQLite
- **Service de traitement** (port 5002) : API qui utilise le service de données pour effectuer des traitements

## Qu'est-ce qu'un Pod Podman ?

Un **pod** dans Podman est un groupe de conteneurs qui :
- Partagent le même espace réseau (localhost)
- Partagent les mêmes volumes 
- Sont démarrés et arrêtés ensemble
- Peuvent communiquer via `localhost` plutôt que par des noms de conteneurs

### Avantages des pods vs conteneurs séparés :

1. **Communication simplifiée** : Les conteneurs dans un pod peuvent se parler via `localhost`
2. **Gestion groupée** : Un seul point de contrôle pour tous les services liés
3. **Isolation réseau** : Le pod forme une unité réseau isolée
4. **Ressources partagées** : Partage efficient des ressources système
5. **Déploiement atomique** : Tous les services du pod démarrent ensemble

## Utilisation

### Prérequis
```bash
# Installer podman et podman-compose
sudo apt update
sudo apt install podman podman-compose
```

### Lancement avec les scripts

1. **Démarrer le projet** :
```bash
chmod +x start.sh
./start.sh
```

2. **Tester les services** :
```bash
chmod +x test.sh
./test.sh
```

### Commandes manuelles

1. **Construire et démarrer** :
```bash
podman-compose build
podman-compose up -d
```

2. **Voir les logs** :
```bash
podman-compose logs -f
```

3. **Vérifier l'état** :
```bash
podman-compose ps
podman pod ps
```

4. **Arrêter** :
```bash
podman-compose down
```

## Endpoints disponibles

### Service de données (http://localhost:5001)
- `GET /` : Informations sur le service
- `GET /health` : Vérification de santé
- `POST /query` : Exécuter une requête SQL

### Service de traitement (http://localhost:5002)
- `GET /` : Informations sur le service
- `GET /health` : Vérification de santé
- `GET /users/all` : Tous les utilisateurs
- `GET /users/count` : Nombre d'utilisateurs
- `GET /users/domain/<domain>` : Utilisateurs par domaine
- `POST /process` : Requête personnalisée

## Exemple d'utilisation

```bash
# Tester le service de données
curl http://localhost:5001/

# Exécuter une requête SQL
curl -X POST http://localhost:5001/query \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT * FROM users LIMIT 5"}'

# Tester le service de traitement
curl http://localhost:5002/users/count
```

## Dépannage

- **Erreur 404** : Vérifiez que les services sont démarrés avec `podman-compose ps`
- **Communication impossible** : Les services dans le même pod utilisent `localhost` pour communiquer
- **Problème de construction** : Utilisez `podman-compose build --no-cache` pour reconstruire

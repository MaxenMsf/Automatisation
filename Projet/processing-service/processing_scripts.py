import requests
import json

class DataProcessor:
    def __init__(self, api_base_url="http://localhost:5001"):
        self.api_base_url = api_base_url
    
    def send_query(self, query):
        """Envoie une requête SQL au service de données"""
        try:
            response = requests.post(
                f"{self.api_base_url}/query",
                json={"query": query},
                headers={"Content-Type": "application/json"}
            )
            return response.json()
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_all_users(self):
        """Récupère tous les utilisateurs"""
        print("=== Récupération de tous les utilisateurs ===")
        result = self.send_query("SELECT * FROM users")
        if result.get("success"):
            users = result.get("data", [])
            print(f"Nombre d'utilisateurs trouvés: {len(users)}")
            for user in users:
                print(f"ID: {user['id']}, Nom: {user['name']}, Email: {user['email']}")
        else:
            print(f"Erreur: {result.get('error')}")
        return result
    
    def count_users(self):
        """Compte le nombre d'utilisateurs"""
        print("=== Comptage des utilisateurs ===")
        result = self.send_query("SELECT COUNT(*) as total FROM users")
        if result.get("success"):
            total = result.get("data", [{}])[0].get("total", 0)
            print(f"Nombre total d'utilisateurs: {total}")
        else:
            print(f"Erreur: {result.get('error')}")
        return result
    
    def get_users_by_domain(self, domain):
        """Récupère les utilisateurs par domaine email"""
        print(f"=== Utilisateurs avec le domaine {domain} ===")
        query = f"SELECT * FROM users WHERE email LIKE '%@{domain}%'"
        result = self.send_query(query)
        if result.get("success"):
            users = result.get("data", [])
            print(f"Utilisateurs trouvés: {len(users)}")
            for user in users:
                print(f"Nom: {user['name']}, Email: {user['email']}")
        else:
            print(f"Erreur: {result.get('error')}")
        return result

def main():
    """Script principal qui affiche toutes les données"""
    processor = DataProcessor()
    
    print("🔄 Démarrage du traitement des données...\n")
    
    # Récupérer tous les utilisateurs
    processor.get_all_users()
    print()
    
    # Compter les utilisateurs
    processor.count_users()
    print()
    
    # Chercher par domaine
    processor.get_users_by_domain("example.com")
    print()
    
    print("✅ Traitement terminé!")

if __name__ == "__main__":
    main()
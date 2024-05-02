# Partie 1 : Requête à l'API et enregistrement des résultats dans un fichier JSON
import requests
import json

url = "https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Vérifier si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Obtenir les données de réponse au format JSON
    data = response.json()
    
    # Enregistrer les données brutes dans un fichier JSON
    with open("data_from_api.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
else:
    print("Erreur lors de la requête à l'API.")

# Partie 2 : Traitement des résultats de la requête et enregistrement dans un fichier JSON
if response.status_code == 200:
    # Filtrer les adresses par région et département
    addresses_occitanie = []
    addresses_pyrenees_orientales = []
    addresses_loire_atlantique = []
    
    for result in data['features']:
        properties = result['properties']
        if properties['context'] == 'Occitanie':
            addresses_occitanie.append(properties['label'])
        elif properties['context'] == '66, Pyrénées-Orientales, Occitanie, France':
            addresses_pyrenees_orientales.append(properties['label'])
        elif properties['context'] == '44, Loire-Atlantique, Pays de la Loire, France':
            addresses_loire_atlantique.append(properties['label'])
    
    # Créer un dictionnaire avec les adresses filtrées
    filtered_addresses = {
        "Occitanie": addresses_occitanie,
        "Pyrénées-Orientales": addresses_pyrenees_orientales,
        "Loire-Atlantique": addresses_loire_atlantique
    }
    
    # Enregistrer les adresses filtrées dans un fichier JSON
    with open("filtered_addresses.json", "w") as json_file:
        json.dump(filtered_addresses, json_file, indent=4)
else:
    print("Erreur lors de la requête à l'API.")

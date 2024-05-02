import requests

url = "https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


import requests

# Définir l'URL de l'API avec l'adresse que vous recherchez
url = "https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port"

# Effectuer la requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Obtenir les données de réponse au format JSON
    data = response.json()
    
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
    
    # Afficher les adresses trouvées
    print("Adresses en Occitanie :")
    for address in addresses_occitanie:
        print(address)
    
    print("\nAdresses dans les Pyrénées-Orientales :")
    for address in addresses_pyrenees_orientales:
        print(address)
    
    print("\nAdresses en Loire-Atlantique :")
    for address in addresses_loire_atlantique:
        print(address)
else:
    print("Erreur lors de la requête à l'API.")


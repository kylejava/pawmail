import json
import requests

def getDogPhoto():
    url = "https://dog.ceo/api/breeds/image/random"
    data = requests.get(url)
    json_data = data.json()
    img = json_data['message']
    return img

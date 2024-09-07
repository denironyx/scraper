from dotenv import load_dotenv
import os
import json
from requests import get, post
import base64
load_dotenv()

# get the environment variable
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

## Authorization
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    # spotify url
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = get_token()

# create authorization header
def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}

# get list of Nigeria artists
afrobeats_artists = [
    "Davido",
    "Wizkid",
    "Burna Boy",
    "Asake",
    "Tiwa Savage",
    "Olamide",
    "Yemi Alade",
    "Rema",
    "Fireboy DML",
    "Naira Marley",
    "Joeboy",
    "Mr Eazi",
    "Tems",
    "Patoranking",
    "Tekno",
    "Adekunle Gold",
    "Flavour",
    "Kizz Daniel",
    "Mayorkun",
    "Simi",
    "Falz",
    "Omah Lay",
    "Teni",
    "CKay",
    "Zlatan",
    "Peruzzi"
]

## search for artists
def search_for_artist(token, artist_name):
    print("Searching for artist: " + artist_name)
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&market=NG&limit=1"
    query_url = url + query
    result = get(query_url, headers = header)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artists found.")

    return json_result[0]

## create an empty dictionary
all_artist_data = []

## a for loop that fetches artist
for artist in afrobeats_artists:
    artist_data = {}
    result = search_for_artist(token, artist)

    if result:
        artist_data["artist_name"] = result["name"]
        artist_data["artist_id"] = result["id"]
        artist_data["popularity"] = result["popularity"]
        artist_data["followers"] = result["followers"]["total"]

        ## add the data to the dictionary
        all_artist_data.append(artist_data)

for artist in all_artist_data:
    print(artist["artist_name"])

# Specify the Directory to save the file
# Save the data to a JSON file
with open('../data/nigerian_artists_data.json', 'w') as f:
    json.dump(all_artist_data, f, indent=4)
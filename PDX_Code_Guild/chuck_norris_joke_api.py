import requests
# Access the chuck norris joke database API
resp = requests.get('http://api.icndb.com/jokes/random')
# Convert response to json and grab the joke
print(resp.json()['value']['joke'])
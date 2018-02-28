import requests
import json

# TODO: replace with your own app_id and app_key
app_id = 'f4959b56'
app_key = 'b21f533facf3f53a29016ff1b78b702f'

language = 'en'
word_id = 'test'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
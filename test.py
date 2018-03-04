import requests
import json
import random

app_id = 'f4959b56'
app_key = 'b21f533facf3f53a29016ff1b78b702f'

#Parses a new URL for the given input
def parseURL(lang, lexCat, wordLimit):

    maxWords = {
        'adjective': 47654,
        'noun': 0,
        'verb': 0
    }

    #Generates a random selection for the word category
    offset = str(random.randint(0, maxWords.get(str(lexCat), "")))
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + lang + '/lexicalCategory=' + lexCat.lower() + '?offset=' + offset + '&limit=' + str(wordLimit)
    return url


#Gets the JSON response from given URL
r = requests.get(parseURL('en', 'adjective', '1'), headers = {'app_id': app_id, 'app_key': app_key})

adjective = r.json()['results'][0].get('word', '')
print(adjective)
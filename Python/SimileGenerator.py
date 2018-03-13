import requests
import json
import random

app_id = 'f4959b56'
app_key = 'b21f533facf3f53a29016ff1b78b702f'

#Parses a new URL for the given input
def parseURL(lang, lexCat, wordLimit, wordFreq):

    maxWords = {
        'adjective': 47654,
        'adverb': 8882,
        'conjunction': 69,
        'noun': 158519,
        'numeral': 90,
        'preposition': 175,
        'verb': 15225,
    }

    #Generates a random selection for the word category
    offset = str(random.randint(0, maxWords.get(str(lexCat), "")))
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + lang + '/lexicalCategory=' + lexCat.lower() + '?offset=' + offset + '&limit=' + str(wordLimit)
    #urlWithFreq = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + lang + '/lexicalCategory=' + lexCat.lower() + '?corpus=nmc&minFrequency=' + str(wordFreq) + '?offset=' + offset + '&limit=' + str(wordLimit)
    return url

def makeRequest(lang, lexCat, wordLimit, wordFreq, app_id, app_key):

    return requests.get(parseURL(lang, lexCat, wordLimit, wordFreq), headers={'app_id': app_id, 'app_key': app_key}).json()['results'][0].get('word', '')

def simileGenerator(simileWord):
    # TODO: generate strings to display in a sensical way.
    returnString = ""

    # Gets the JSON response from given URL
    adjective = makeRequest('en', 'adjective', '1', 100, app_id, app_key)
    adjective2 = makeRequest('en', 'adjective', '1', 100, app_id, app_key)
    noun = makeRequest('en', 'noun', '1', 100, app_id, app_key)
    noun2 = makeRequest('en', 'noun', '1', 100, app_id, app_key)
    preposition = makeRequest('en', 'preposition', '1', 100, app_id, app_key)

    returnString += simileWord + " is " + adjective + "er than a " + adjective2 + " " + noun + " " + preposition + " a " + noun2

    return returnString


print(simileGenerator("Peter"))

#print(makeRequest('en', 'adjective', '1', 100, app_id, app_key))


#Run code below to check amounts of words in categories. Switch the last param
#url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/en/lexicalCategory=verb'
#r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
#print(r.json()['metadata'])
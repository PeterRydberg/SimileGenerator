function parseURL(lang, lexCat, wordLimit, wordFreq){
    maxWords = {
        'adjective': 47654,
        'adverb': 8882,
        'conjunction': 69,
        'noun': 158519,
        'numeral': 90,
        'preposition': 175,
        'verb': 15225
    };

    // Generates a random selection for the word category
    offset = Math.round(Math.random() * maxWords[lexCat.toLowerCase()]);
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + lang + '/lexicalCategory=' + lexCat.toLowerCase() + '?offset=' + offset + '&limit=' + wordLimit;
    //urlWithFreq = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/' + lang + '/lexicalCategory=' + lexCat.toLowerCase() + '?corpus=nmc&minFrequency=' + str(wordFreq) + '?offset=' + offset + '&limit=' + str(wordLimit)
    return url
}

//function httpAsyncRequest(url, callback){
//    var req = new XMLHttpRequest();
//
//    req.onreadystatechange = function() {
//        if(req.readyState == 4 && req.status == 200)
//            callback(req.responseText);
//    }
//
//    req.open('GET', parseURL, true);
//    req.send();
//    return req.responseText
//}

function makeRequest(lang, lexCat, wordLimit, wordFreq, app_id, app_key){
    url = parseURL(lang, lexCat, wordLimit, wordFreq);
    console.log(url);

    fetch(url, {
        headers: {
            'app_id': app_id,
            'app_key': app_key
        }
    })
        .then((resp) => resp.json())
        .then(function (data) {
            let returnData = data.results;
            return data;
    })
}

function simileGenerator(app_id, app_key, simileWord) {
    returnString = '';

    // Gets the JSON response from given URL
    adjective = makeRequest('en', 'adjective', '1', 100, app_id, app_key);
    /*adjective2 = makeRequest('en', 'adjective', '1', 100, app_id, app_key);
    noun = makeRequest('en', 'noun', '1', 100, app_id, app_key);
    noun2 = makeRequest('en', 'noun', '1', 100, app_id, app_key);
    preposition = makeRequest('en', 'preposition', '1', 100, app_id, app_key);

    returnString += simileWord + ' is ' + adjective + 'er than a ' + adjective2 + ' ' + noun + ' ' + preposition + ' a ' + noun2;

    alert(returnString);*/
    alert(adjective);
}

simileGenerator('f4959b56', 'b21f533facf3f53a29016ff1b78b702f', 'Peter');
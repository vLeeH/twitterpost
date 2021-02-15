# Search post in the terminal

import os
import urllib.parse
import json
try:
    import oauth2
except ImportError: 
    os.system("pip install requirements.txt")
import pprint

# Note: don't forget to create an app in developer portal of Twitter https://developer.twitter.com/en

# Secret and Api key of Twitter app 
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

# Token key and secret of Twitter app 
token_key = os.getenv('TOKEN_KEY')
token_secret = os.getenv('TOKEN_SECRET')


consumer = oauth2.Consumer(api_key, secret_key) # access the account
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token) # gather the information of the account 

query = str(input('Search:'))
query_codificada = urllib.parse.quote(query, safe='')

requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')
decodificar = requisicao[1].decode() # transform in string 

objeto = json.loads(decodificar)
twitts = objeto['statuses']

for twitt in twitts:
    print(twitt['user']['screen_name'])
    print(twitt['text'])

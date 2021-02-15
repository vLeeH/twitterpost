import os 
import oauth2
import json

import urllib.parse

class Twitter: 
    def __init__(self, api_key, secret_key, token_key, token_secret): 
        self.connection(api_key, secret_key, token_key, token_secret)

    
    def connection(self, api_key, secret_key, token_key, token_secret):
        self.consumer = oauth2.Consumer(api_key, secret_key) 
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)


    def tweet(self, new_tweet): 
        query_codificada = urllib.parse.quote(new_tweet, safe='')
        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

        decodificar = requisicao[1].decode() 

        objeto = json.loads(decodificar)

        return objeto

    
    def search(self, query, lang):
        query_codificada = urllib.parse.quote(query, safe='')

        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=' + lang)
        decodificar = requisicao[1].decode() 

        objeto = json.loads(decodificar)
        twitts = objeto['statuses']

        return twitts

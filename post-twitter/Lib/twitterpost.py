import os 
import oauth2
import json

import urllib.parse

class Twitter: 
    def __init__(self, api_key, secret_key, token_key, token_secret): 
        """Set the keys"""
        self.connection(
            api_key, secret_key, token_key, token_secret)

    
    def connection(self, api_key, secret_key, token_key, token_secret):
        """Connect with the keys"""
        self.consumer = oauth2.Consumer(api_key, secret_key) 
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)


    def tweet(self, new_tweet): 
        """Post a tweet using the terminal
        - Put the method = POST, to indicate the type of method
        - Get the api of statuses/update """
        query_codificate = urllib.parse.quote(new_tweet, safe='')
        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificate, method='POST')

        decodificate = requisicao[1].decode() 

        objeto = json.loads(decodificate)

        return objeto

    
    def search(self, query, lang):
        """Search for tweets.
        - Get the api of search/tweets 
        - lang = the lang of the search 
        - twitts = objeto['statuses'] - just get the statuses """
        query_codificate = urllib.parse.quote(query, safe='')

        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificate + '&lang=' + lang)
        decodificate = requisicao[1].decode() 

        objeto = json.loads(decodificate)
        twitts = objeto['statuses']

        return twitts

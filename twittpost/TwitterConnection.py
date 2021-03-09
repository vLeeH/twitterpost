# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2019-2020 vLeeH
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import os 
import oauth2
import json

import urllib.parse

""" 
VERSION: 0.0.1
"""

class Twitter: 
    def __init__(self, api_key, secret_key, token_key, token_secret): 
        """Set the token keys of your Twitter App"""
        self.connection(
            api_key, secret_key, token_key, token_secret)

    
    def connection(self, api_key, secret_key, token_key, token_secret):
        """Connect with the token keys of your Twitter App."""
        self.consumer = oauth2.Consumer(api_key, secret_key) 
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)


    def tweet(self, new_tweet): 
        """Post a tweet using the terminal:
        - Put the method = POST, to indicate the type of method
        - Get the api of statuses/update """
        query_codificate = urllib.parse.quote(new_tweet, safe='')
        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificate, method='POST')

        decodificate = requisicao[1].decode() 

        objeto = json.loads(decodificate)

        return objeto

    
    def search(self, query, lang):
        """Searching for tweets:
        - Get the api of search/tweets
        - lang = the language of the search
        - twitts = objeto['statuses'] - get the statuses """
        query_codificate = urllib.parse.quote(query, safe='')

        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificate + '&lang=' + lang)
        decodificate = requisicao[1].decode() 

        objeto = json.loads(decodificate)
        twitts = objeto['statuses']

        return twitts

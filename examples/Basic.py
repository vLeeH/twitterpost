"""
-*- coding utf-8 -*-
[INFO]
Don't forget to create an Developer account in Twitter

[IMPORTANT]
api_key - is the api key of your app in Twitter api.
secret_key - is the secret key of your app in Twitter api.
token_key - is the token key of your app in Twitter api.
token_secret - is the token secret of your app in Twitter api.
"""

from twittposter import Twitter
import os 

api_key = API_KEY
secret_key = SECRET_KEY
token_key = TOKEN_KEY
token_secret = TOKEN_SECRET


twitter = Twitter(api_key, secret_key, token_key, token_secret)

# Post the tweet 
resp = twitter.tweet('test')
pprint.pprint(resp)

# Search for tweet
searching = twitter.search('brasil', 'pt')

for result in searching:
    print(f"{result['user']['screen_name']}:")
    print(result['text'])
    print('\n')

print('''
┌┬┐┬ ┬┬┌┬┐┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐┌┬┐
 │ ││││ │  │ ├┤ ├┬┘├─┘│ │└─┐ │ 
 ┴ └┴┘┴ ┴  ┴ └─┘┴└─┴  └─┘└─┘ ┴  by: vLeeH
''')

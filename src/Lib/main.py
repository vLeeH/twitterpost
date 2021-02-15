from Twitterlib import Twitter
import os 
import pprint

# Secret and Api key of Twitter app 
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

# Token key and secret of Twitter app 
token_key = os.getenv('TOKEN_KEY')
token_secret = os.getenv('TOKEN_SECRET')

twitter = Twitter(api_key, secret_key, token_key, token_secret)

# resp = twitter.tweet('test na lib')
# pprint.pprint(resp)

searching = twitter.search('brasil', 'pt')

for result in searching:
    print(f"{result['user']['screen_name']}:")
    print(result['text'])
    print('\n')
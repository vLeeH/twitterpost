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

from twitterposts import Twitter
import os 
import pprint

api_key = API_KEY
secret_key = SECRET_KEY
token_key = TOKEN_KEY
token_secret = TOKEN_SECRET

twitter = Twitter(api_key, secret_key, token_key, token_secret)

# Post the tweet
while True:
    ask_post1 = str(input('Do you want post a Tweet?[Y/N]')).upper()
    if ask_post1 == 'Y':
        post = str(input('Inform your tweet: ')) 
        resp = twitter.tweet(post)
        pprint.pprint(resp)
        print('Tweet posted with success.')
        again_post = str(input('Want to post again?[Y/N] ')).upper()
        if again_post == 'N':
            break

    
# Search for tweet
while True:
    ask_search = str(input('Do you want to search for a Tweet?[Y/N]')).upper()
    if ask_search == 'Y': 
        country = str(input('Which country do you want to search? ')).lower()
        language = str(input('And wich language do you want search? ')).lower()
        searching = twitter.search(country, language)

        for result in searching:
            print(f"{result['user']['screen_name']}:")
            print(result['text'])
            print('\n')

        print('Tweets searched with success.')
        again_search = str(input('Want to search again?[Y/N] ')).upper()
        if again_search == 'N':
            break 
    

print('''
┌┬┐┬ ┬┬┌┬┐┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐┌┬┐
 │ ││││ │  │ ├┤ ├┬┘├─┘│ │└─┐ │ 
 ┴ └┴┘┴ ┴  ┴ └─┘┴└─┴  └─┘└─┘ ┴  by: vLeeH
''')

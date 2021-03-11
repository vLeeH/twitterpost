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
import pprint
from time import sleep

api_key = API_KEY
secret_key = SECRET_KEY
token_key = TOKEN_KEY
token_secret = TOKEN_SECRET

twitter = Twitter(api_key, secret_key, token_key, token_secret)

def menu(): 
    print('''
    ┌┬┐┬ ┬┬┌┬┐┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐┌┬┐
     │ ││││ │  │ ├┤ ├┬┘├─┘│ │└─┐ │ 
     ┴ └┴┘┴ ┴  ┴ └─┘┴└─┴  └─┘└─┘ ┴  by: vLeeH
    ''')


# Post the tweet
def post_tweet():
    while True:
        ask_post1 = str(input('Do you want post a Tweet[Y/N]? ')).upper().strip()
        if ask_post1 == 'Y':
            try: 
                sleep(1)
                post = str(input('Inform your tweet: ')) 
                resp = twitter.tweet(post)
                try:
                    with open("tweet_posted.txt","at+", encoding="utf8") as t: 
                        t.write(
                            f" - {post}")
                except UnicodeDecodeError as u:
                    print(f"[ERROR] - {u}")

                pprint.pprint(resp)
                sleep(1)
                print('Tweet posted with success.')
                sleep(1)
                again_post = str(input('Want to post again[Y/N]? ')).upper().strip()
                if again_post == 'N':
                    break
            except Exception as e: 
                print(e)
        
        else:
            break

    
# Search for tweet
def post_search():
    while True:
        ask_search = str(input('Do you want to search for a Tweet[Y/N]? ')).upper().strip()
        if ask_search == 'Y': 
            sleep(1)
            country = str(input('Which country do you want to search? ')).lower().strip()
            language = str(input('And wich language do you want search? ')).lower().strip()
            
            # Use the funtion of twittlib to search for posts
            searching = twitter.search(country, language)
            for result in searching:
                print(f"{result['user']['screen_name']}:")
                print(f"{result['text']} \n")
                try:
                    with open("results.txt","at+", encoding="utf8") as t: 
                        t.write(
                            f"{result['text']}")
                except UnicodeDecodeError as u:
                    print(f"[ERROR] - {u}")

            sleep(1)
            print('Tweets searched with success.')
            sleep(1)
            again_search = str(input('Want to search again?[Y/N] ')).upper().strip()
            if again_search == 'N':
                break

        else:
            break
        

menu()
post_tweet()
post_search()
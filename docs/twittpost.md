# 📄 Twittpost 
Welcome to **twittpost's Documentation**. 

## Functionally
Twittpost is a simple library for Twitter API, that create and search posts.<br>
<a href="https://github.com/vLeeH/twittpost/blob/main/twitterpost/TwitterConnection.py">↳ Source Code</a>

## Important
You need to create an account/developer account in Twitter, after that need to create an app in Developer portal of Twitter.

### Variables 
**Secret and api key of Twitter app**
- api_key 
- secret_key 

**Token key and secret of Twitter app**
- token_key 
- token_secret 

### URL's
**API References** (Developer portal)
- <a href="https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets">Search Tweets</a>
- <a href="https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update">Doing posts</a>

## Installation
**twittpost requires Python 3.7+**

**Windows**
```
py -3.8 -m pip install twittpost
```

**Linux**
```
python3.8 -m pip install twittpost
```

## Getting Started
A **quick** and **easy** post and searching in twitter example:
```python
    from twitterpost import Twitter
    import pprint

    api_key = API_KEY
    secret_key = SECRET_KEY
    token_key = TOKEN_KEY
    token_secret = TOKEN_SECRET

    twitter = Twitter(api_key, secret_key, token_key, token_secret)

    resp = twitter.tweet('test')
    pprint.pprint(resp)

    searching = twitter.search('brasil', 'pt')

    for result in searching:
        print(f"{result['user']['screen_name']}:")
        print(result['text'])
        print('\n')
```

Dating in a log.txt the search and posts 
```python
from twittpost import Twitter
import os 
import pprint
from time import sleep

api_key = API_KEY
secret_key = SECRET_KEY
token_key = TOKEN_KEY
token_secret = TOKEN_SECRET

twitter = Twitter(api_key, secret_key, token_key, token_secret)

# Post the tweet
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
while True:
    ask_search = str(input('Do you want to search for a Tweet[Y/N]? ')).upper().strip()
    if ask_search == 'Y': 
        sleep(1)
        country = str(input('Which country do you want to search? ')).lower().strip()
        language = str(input('And wich language do you want search? ')).lower().strip()
        
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
```




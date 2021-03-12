# Twitterposts 
Welcome to **twitterposts's Documentation**. 

## Functionally
Twittpost is a simple library for Twitter API, that create and search posts.<br>
<a href="https://github.com/vLeeH/twittpost/blob/main/twittpost/TwitterConnection.py">↳ Source Code</a>

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

## Explanation
Put the keys/tokens of your Twitter App.
```python
api_key = API_KEY
secret_key = SECRET_KEY
token_key = TOKEN_KEY
token_secret = TOKEN_SECRET
```


Pass the variables in the function.
```python
twitter = Twitter(api_key, secret_key, token_key, token_secret)
```


Publicate a tweet in Twitter.
- In `twitter.tweet('test')` put the message that you want to publicate.


Put the location and the lang that you want to search.
```python
searching = twitter.search('brasil', 'pt')


for result in searching:
    print(f"{result['user']['screen_name']}:")
    print(result['text'])
    print('\n')
```

## Quick example
```python
from twittpost import Twitter
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



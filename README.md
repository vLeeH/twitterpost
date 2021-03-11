# twitterpost
![python](https://img.shields.io/badge/Python-3.7%20%7C%203.8-blue.svg) ![license](https://img.shields.io/github/license/vLeeH/twitterpost.svg) <br>
A Twitter wrapper for the Twitter API that search and do posts in Twitter.

## Documentation
<a href="https://github.com/vLeeH/twittpost/blob/main/docs/twittpost.md">Documentation</a>

## Installations
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

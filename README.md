# Twitterlib
A Twitter library of the Twitter API. 

## Functionallies 
- Search posts in Twitter
- Do posts in Twitter 
- Delete posts in Twitter  

## Installation 
**Python** - 3.8 
```
pip install Twitterlib
```

## Libs 
```
pip install -r requirements.txt
```

## Examples 
- <a href="">Basic</a> code example
- <a href="">Intermediate</a> code example
- <a href="">Advance</a> code example


## Getting Started
A quick and **easy post and searching in twitter** example: 

    from Twitterlib import Twitter
    import os 
    
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
        
        
        

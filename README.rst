Twitterlib - Developing
----

A Twitter library of the Twitter API. 

Functionallies 
---------------------------

- Search posts in Twitter
- Do posts in Twitter 
- Delete posts in Twitter  

Installation 
---------------------------

**Python** - ```3.8``` 

.. code:: sh

    pip install Twitterlib


Libs
---------------------------

.. code:: sh

    pip install -r requirements.txt

Examples
---------------------------

- `Basic <https://github.com/vLeeH/Twitterlib/blob/main/examples/Basic.py#>`_ code example
- `Intermediate <https://github.com/vLeeH/Twitterlib/blob/main/examples/Intermediate.py#>`_ code example
- `Advance <https://github.com/vLeeH/Twitterlib/blob/main/examples/Advance.py#>`_ code example

Getting Started
---------------------------

A quick and **easy post and searching in twitter** example: 

.. code:: py

    from Twitterlib import Twitter
    
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
        
        
        

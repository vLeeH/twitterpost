twitterpost 
=============

.. image:: https://img.shields.io/badge/Python-3.7%20%7C%203.8-blue.svg
    :target: https://www.python.org
    
.. image:: https://img.shields.io/github/license/vLeeH/twitterpost.svg
    :target: LICENSE

A Twitter library for the Twitter API that search and do posts in Twitter.

Installation 
---------------------------

.. code:: sh

    pip install twitterpost

Getting Started
---------------------------

A quick and **easy** post and searching in twitter example: 

.. code:: py

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
        
        
        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use Twython to interface with Twitter API to search recent tweets.
Based on code in Data Science from Scratch by Joel Grus.
"""

movie_query = 'Parasite movie'

from twython import Twython
import webbrowser, json

CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'secret key'

temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()

# Get a temporary client to retrieve an authentication url
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['auth_url']

# Now visit that URL to authorize the application and get a PIN
print("go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")

# Now we use that PIN_CODE to get the actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds['oauth_token'],
                      temp_creds['oauth_token_secret'])
final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN = final_step['oauth_token']
ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']

tweets = twitter.search(q=movie_query,lang='en',count=100)

tweets_json = json.dumps(tweets['statuses'])

with open('tweets.json','w') as f:
    f.write(tweets_json)


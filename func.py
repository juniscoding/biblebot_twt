import os
import tweepy
import json
import random

with open('verses.json') as verses:
    data = json.load(verses)


bot = tweepy.Client(
    #Consumer Keys
    consumer_key= os.environ['CONSUMER_KEY'],
    consumer_secret= os.environ['CONSUMER_SECRET'],
    # Access Token and Secret
    access_token= os.environ['ACCESS_TOKEN'],
    access_token_secret= os.environ['ACCESS_TOKEN_SECRET'])

def post_quote():
    verses = data["verses"]
    print("Load verses...")
    random_index = random.randint(0, len(verses)-1)
    print("Get random index...")
    print(random_index)
    verse = verses[random_index]
    print("Get verse...")
    print(verse)
    r = bot.create_tweet(text=verse)
    return None
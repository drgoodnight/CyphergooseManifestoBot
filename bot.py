import os
import re
import tweepy
import math
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# V2 API Twitter Authentication
def V2_Auth():
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        wait_on_rate_limit=True
    )
    return client

# Function to get a random sentence containing specific words from the file
def get_random_sentence(filename):
    with open(filename, 'r') as file:
        sentences = file.readlines()

    # Filter sentences containing the specific words
    keywords = ['Geese', 'geese', 'goose', 'Dmitri']
    matching_sentences = [sentence for sentence in sentences if any(keyword in sentence for keyword in keywords)]

    if not matching_sentences:
        print("No sentences found containing the specific words.")
        return None

    # Get a random sentence from the filtered list
    sentence = random.choice(matching_sentences).strip()

    return sentence

# Get a random sentence from the file
quote = get_random_sentence('manifesto.txt')

if quote:
    client = V2_Auth()
    
    # If the quote is longer than 200 characters, split it into a thread
    if len(quote) > 200:
        # Calculate the number of tweets needed
        num_tweets = math.ceil(len(quote) / 200)
        
        # Split the quote into parts of 200 characters each
        quote_parts = [quote[i:i + 200] for i in range(0, len(quote), 200)]

        # Tweet each part as a thread
        for i, part in enumerate(quote_parts):
            tweet_text = f'🧵 {i+1}/{num_tweets}👇 "{part}"'
            if i == 0:
                tweet = client.create_tweet(text=tweet_text)
            else:
                tweet = client.create_tweet(text=tweet_text, reply_to=tweet.id)
            print(f"Tweeted: {tweet_text}")
    else:
        # If the quote is less than 200 characters, tweet it normally
        tweet_text = f'"{quote}"'
        client.create_tweet(text=tweet_text)
        print(f"Tweeted: {tweet_text}")
else:
    print("Failed to get a sentence from the file.")

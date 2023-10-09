import os
import random
import re
import tweepy
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
    # Create the tweet text with the quote in quotation marks
    tweet_text = f'"{quote}"'

    # Authenticate and create a tweet
    client = V2_Auth()
    client.create_tweet(text=tweet_text)
    print(f"Tweeted: {tweet_text}")
else:
    print("Failed to get a sentence from the file.")

import os
import random
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

# Function to split the quote into parts without dividing words
def split_quote(quote, length):
    words = quote.split()
    parts = []
    current_part = ''

    for word in words:
        if len(current_part) + len(word) + 1 <= length:
            current_part += ' ' + word
        else:
            parts.append(current_part.strip())
            current_part = word

    parts.append(current_part.strip())
    return parts

# Get a random sentence from the file
quote = get_random_sentence('manifesto.txt')

if quote:
    client = V2_Auth()
    
    # If the quote is longer than 200 characters, split it into a thread
    if len(quote) > 200:
        # Split the quote into parts without dividing words
        quote_parts = split_quote(quote, 200)

        # Calculate the number of tweets needed
        num_tweets = len(quote_parts)

        # Tweet each part as a thread
        for i, part in enumerate(quote_parts):
            tweet_text = f'🧵 {i+1}/{num_tweets}👇 "{part}"'
            if i == 0:
                response = client.create_tweet(text=tweet_text)
                tweet_data = response.data
            else:
                response = client.create_tweet(text=tweet_text, in_reply_to_tweet_id=previous_tweet_id)  # Reply to the previous tweet ID
                tweet_data = response.data
            
            print(f"Tweeted: {tweet_text}")
            previous_tweet_id = tweet_data['id']  # Store the ID of the current tweet for the next iteration
    else:
        # If the quote is less than 200 characters, tweet it normally
        tweet_text = f'"{quote}"'
        client.create_tweet(text=tweet_text)
        print(f"Tweeted: {tweet_text}")
else:
    print("Failed to get a sentence from the file.")

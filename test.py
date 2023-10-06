import tweepy
import schedule
import time
import random
from decouple import Config
import logging

# Set up logging
logging.basicConfig(filename='errors.log', level=logging.ERROR)

# Load credentials from .env file
config = Config()
API_KEY = config('API_KEY')
API_SECRET_KEY = config('API_SECRET_KEY')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Load the provided text from a file
with open('manifesto.txt', 'r') as file:
    text = file.read()

# Split the text into sentences
sentences = text.split('.')

# Function to post a random pair of consecutive sentences on Twitter
def post_random_sentence():
    index = random.randint(0, len(sentences) - 2)  # Adjust index range to prevent IndexError
    sentence_pair = sentences[index].strip() + ". " + sentences[index + 1].strip() + "."
    tweet = (
        "Hi, this is the GooseManifestoBot. Do not forget the reason we keep grinding. "
        f"Let me remind you with a quote from our 'A Cyphergoose's Manifesto': {sentence_pair}"
    )
    try:
        api.update_status(tweet)
        print(f"Posted: {tweet}")
    except tweepy.TweepError as e:
        error_message = f"Error: {e.reason}"
        print(error_message)
        logging.error(error_message)
        if 'Rate limit exceeded' in e.reason:
            print("Rate limit exceeded. Waiting...")
        else:
            print("An error occurred. Waiting for 5 minutes before retrying...")
            time.sleep(300)  # Wait for 5 minutes before retrying

# Schedule the function to run every 5 minutes
schedule.every(5).minutes.do(post_random_sentence)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

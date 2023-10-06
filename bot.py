import tweepy
import schedule
import time
import random
from decouple import Config

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
with open('text.txt', 'r') as file:
    text = file.read()

# Extract sentences containing "Geese"
sentences = [sentence.strip() for sentence in text.split('.') if 'Geese' in sentence]

# Function to post a random sentence on Twitter
def post_random_sentence():
    sentence = random.choice(sentences)
    tweet = (
        "Hi, this is the GooseManifestoBot. Do not forget the reason we keep grinding. "
        f"Let me remind you with a quote from our 'A Cyphergoose's Manifesto': {sentence}"
    )
    try:
        api.update_status(tweet)
        print(f"Posted: {tweet}")
    except tweepy.TweepError as e:
        print(f"Error: {e.reason}")
        if 'Rate limit exceeded' in e.reason:
            print("Rate limit exceeded. Waiting...")
        else:
            print("An error occurred. Waiting for 5 minutes before retrying...")
            time.sleep(300)  # Wait for 5 minutes before retrying

# Schedule the function to run daily at a specific time, e.g., 12:00
schedule.every().day.at("12:00").do(post_random_sentence)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

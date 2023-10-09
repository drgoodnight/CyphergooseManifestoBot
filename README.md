# CyphergooseManifestoBot
The bot is designed to automatically post a tweet on X every day at a specified time. Each tweet will contain a randomly selected sentence from "A Goose's Manifesto".


Capabilities of the Script

    Environment Variable Loading:
        The script loads environment variables from a .env file, which should contain Twitter API credentials.

    Twitter API Authentication:
        It authenticates with the Twitter API using the credentials loaded from the .env file.

    Random Sentence Retrieval:
        The script retrieves a random sentence containing specific keywords (e.g., 'Geese', 'geese', 'goose', 'Dmitri') from a text file named 'manifesto.txt'.

    Tweet Creation:
        If the retrieved sentence is less than 200 characters, it tweets the sentence directly.
        If the sentence is longer than 200 characters, it splits the sentence into multiple parts, ensuring words are not divided, and tweets each part as a thread.

    Threaded Tweets:
        When tweeting a long sentence in parts, each subsequent tweet is a reply to the previous one, creating a Twitter thread.

    Error Handling:
        It handles the case where no sentences containing the specific keywords are found in the 'manifesto.txt' file.

Setting Up Locally

    Clone the Repository:
        Clone the repository containing the script to your local machine.

    Install Dependencies:
        You need Python installed on your machine. You can download it from python.org.
        Install the required Python packages. Open a terminal, navigate to the directory containing the script, and run:

        bash

    pip install tweepy python-dotenv

Set Up Environment Variables:

    Create a .env file in the same directory as the script.
    Add your Twitter API credentials to the .env file in the following format:

    env

    CONSUMER_KEY=your_consumer_key
    CONSUMER_SECRET=your_consumer_secret
    ACCESS_TOKEN=your_access_token
    ACCESS_TOKEN_SECRET=your_access_token_secret
    BEARER_TOKEN=your_bearer_token

Add the Text File:

    Ensure there is a text file named 'manifesto.txt' in the same directory as the script. This file should contain sentences from which the script will select randomly.

Run the Script:

    In the terminal, navigate to the directory containing the script and run:

    bash

    python3 bot.py

    The script will select a random sentence from 'manifesto.txt' and tweet it. If the sentence is longer than 200 characters, it will split it into multiple tweets and create a thread.

Verify the Tweet:

    Check your Twitter account to verify that the tweet or thread has been posted.

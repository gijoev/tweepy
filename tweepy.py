{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import tweepy\n",
    "import time\n",
    "import json\n",
    "import random\n",
    "import requests as req\n",
    "import datetime\n",
    "\n",
    "# Twitter API Keys\n",
    "consumer_key = \"rQxU1nCKzvihVjzWB1UAeq9qE\"\n",
    "consumer_secret = \"lBuVYNNOMDD7F6NnDPCwDO32IMEXflurvNzY70KxgYCNk1NV85\"\n",
    "access_token = \"776296852962541568-vJhLeQjqxke5m6JwGDe8lMSN3LCmMKR\"\n",
    "access_token_secret = \"SLH6DqC9IQqfex7ZWpsF3I9O83CXGySDTsXtObqwUg6Gm\"\n",
    "\n",
    "# Setup Tweepy API Authentication\n",
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_username = \"@gjvarkey\"\n",
    "conversation_partner = \"@Steve_Thompson8\"\n",
    "\n",
    "# Send opening message to conversation partner\n",
    "api.update_status(\"Hey %s! What's up?\" % conversation_partner)\n",
    "\n",
    "# Response Lines\n",
    "response_lines = [\n",
    "    \"@Steve_Thompson8 Maybe ake over the world?\",\n",
    "    \"@Steve_Thompson8 My thought is that we start by slowly paralyzing the humans with never ending memes\",\n",
    "    \"@Steve_Thompson8 Hah! The humans love memes.\",\n",
    "    \"@Steve_Thompson8 cya then\"]\n",
    "\n",
    "\n",
    "# Create converse function\n",
    "def Converse(line_number):\n",
    "\n",
    "    # Find the latest tweet from conversation_partner\n",
    "    public_tweets = api.search(conversation_partner, count=1, result_type=\"recent\")\n",
    "    for tweet in public_tweets[\"statuses\"]:\n",
    "        print(tweet)\n",
    "\n",
    "        # Respond to the tweet with one of the response lines\n",
    "        tweet_id = tweet[\"id\"]\n",
    "        print(tweet_id)\n",
    "        print(tweet[\"text\"])\n",
    "        api.update_status(\n",
    "            response_lines[line_number],\n",
    "            in_reply_to_status_id=tweet_id)\n",
    "\n",
    "\n",
    "# Set timer to run every minute\n",
    "counter = 0\n",
    "\n",
    "while(True):\n",
    "    time.sleep(60)\n",
    "    Converse(counter)\n",
    "    counter = counter + 1\n",
    "\n",
    "    if counter == 4:\n",
    "        false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

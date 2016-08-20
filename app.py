from flask import Flask, request
import tweepy
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
    
@app.route("/json_example")
def json_example():
    return json.dumps({
        'key': 'value'
    })

@app.route("/twitter")
def twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    query = 'Donald Trump'
    max_tweets = 2
    searched_tweets = api.search(q=query, count=max_tweets)
    return json.dumps(searched_tweets)

@app.route("/request_example")
def request_example():
    return "You entered {} from the url".format(request.args.get('input'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

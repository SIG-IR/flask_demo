from flask import Flask, request
import requests
import tweepy
from bs4 import BeautifulSoup
from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
    
@app.route("/html")
def html():
    return "<h3>Hello <i>World</i></h3>"
    
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

@app.route("/bs4")
def bs4():
    html = requests.get('http://www.politico.com/2016-election/results/map/president/illinois')
    soup = BeautifulSoup(html.text, "html.parser")
    democrat_percentages = soup.findAll("tr", { "class": "type-democrat" })
    result = [p.getText() for p in democrat_percentages]
    return json.dumps(result)

@app.route("/request_example")
def request_example():
    return "You entered {} from the url".format(request.args.get('input'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

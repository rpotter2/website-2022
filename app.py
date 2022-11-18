import tweepy
from flask import Flask, render_template
from credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET_KEY

app = Flask(__name__)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
username = 'IBMpoembot'
tweets_list = api.user_timeline(screen_name=username, count=3, include_rts=False,
                                tweet_mode='extended')  # Get the last 3 tweets
poem1 = tweets_list[0].full_text
poem2 = tweets_list[1].full_text
poem3 = tweets_list[2].full_text

poem1 = poem1.split('\n')
poem2 = poem2.split('\n')
poem3 = poem3.split('\n')


@app.route('/')
def index():
    return render_template('home.html', poem1=poem1, poem2=poem2, poem3=poem3)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

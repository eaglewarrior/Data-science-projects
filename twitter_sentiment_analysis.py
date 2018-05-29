import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'JE79WsUY5Cln1BYzzNvu1owLd'
consumer_secret= 'Q7zvLeVFPaCxnjswkDBMyT4awl2hTqkYEnDtHwgIdBZ77HU5Xs'

access_token='2471239567-zh0TlaYfZXmFF1d4E6r6We1Ahpb1xKdR9D1b4os'
access_token_secret='1cYtvMq0rM9V0MQf7MPdjmiqT0XcW8Y5q4nvY0AtQa0Yz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

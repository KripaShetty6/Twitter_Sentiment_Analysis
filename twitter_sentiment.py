import tweepy
from textblob import TextBlob
#copied from app.twitter after making your own api
consumer_key =	'zFjG7gIOnaGBnGxAuBMrA6BE9'
consumer_secret = 	'v8ICK5l4s9xs8XbLs8ZS00D4WlWrmm2O23ZsmuhkMGYdGUbB9u'

access_token = '2420202108-kKMgtbYkmlhNdDEq9UtQ6FEMQNUNlW7nJeHI0bc'
access_token_secret = 'tvZZLiN4LR9OMaypAPApx6kUo34n6zcI6l7QJkXyiKLIa'

#tweepy library access code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#used to print just the tweets having the follwing keyword 
public_tweets = api.search('Trump')
for tweet in public_tweets:
    print (tweet.text)
    #print #blank line 
    
    
    #sentiment analysis code 
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print  #blank line 
    
    


#run using
# python progmname.py on terminal 

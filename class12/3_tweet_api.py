import tweepy

consumer_key=''
consumer_secrate=''

access_token=''
access_token_secrate=''
auth=tweepy.OAuthHandler(consumer_key,consumer_secrate)
auth.set_access_token(access_token,access_token_secrate)
api=tweepy.API(auth)
hash_tag=input("enter the hash tag to search")
number=input("enter number of tweets you want to see")
tweets=api.search(hash_tag,lang="en",count=number,tweet_mode="extended")
for tweet in tweets:
    print("_"*10)
    print(tweet.full_text)
    print("_"*10)
import tweepy

consumer_key='wF1H7VZkQgydYdhZwbaiXv2Bh'
consumer_secrate='8rL4K3kKMFQ8RUd3RBiH9LHDKzO1xf6dOfYnYzF6qqugbS7Yot'

access_token='714260025384960000-YXkzwcfmIdL59N0Rrr3n36xkTpNqPHK'
access_token_secrate='JjVBq4pPbs3Q8vlVMLWA3TmBDzZI7NWps3xSlD5PL5CFR'
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
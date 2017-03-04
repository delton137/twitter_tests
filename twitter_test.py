import tweepy
import jason 


CONSUMER_KEY = 'RJlT16JiP4TAGvPP2wvLtDJxS'
CONSUMER_SECRET = 'oZUuiLZ4GHp70inCw6tvzN7qQjB532ObCxXiGVHTcy937KnFyQ'
ACCESS_TOKEN = '203639204-pLm2Uv0lKyfavJDutVwnjwBkXMCZjOqxnppqjdZP'
ACCESS_SECRET = 'GkPJxWV4GLbj7d9aBVJOEczGKhYi8qUCB8qbd8VuB2SkH'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twitter_stream = TwitterStream(auth=oauth)


def get_all_tweets(screen_name, api):
   
    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name, count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))
       
    #write tweet objects to JSON
    file = open('tweet.json', 'wb') 
    print "Writing tweet objects to JSON please wait..."
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print "Done"
    file.close()

if __name__ == '__main__':
    get_all_tweets("@realDonaldTrump")











# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
#tweet_count = 1000
#for tweet in iterator:
#    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
#    print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
#    if tweet_count <= 0:
#        break 
import sys
import csv #required packages if you dont have tweepy in cmd type pip install tweepy
import tweepy

consumer_key = ""
consumer_secret = "" #your twitter app credentials
access_key = ""
access_secret = ""

#function to get 100 tweets max is 3204 
def get_tweets(username):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#maam you can set your limit here
	numberOfTweets = 3200

	tweets = api.user_timeline(screen_name = username,count = numberOfTweets)

	for x in tweets:
		print x.text

	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
	
	#write to a new csv file from the array of tweets
	print "writing to {0}_tweets.csv".format(username)
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)



if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
    	get_tweets(sys.argv[1])
    else:
        print "Error parsing"

 

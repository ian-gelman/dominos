import time
import tweepy

target = '@dominos'

consumer_key = 'zhcs14gsC2zEVQditWMP5zyjO'
consumer_secret = 'W7yMSsTBFncspY6MhjmjENSbvSKOlKLcWuhxw8LIqLv4TOdbYp'
access_token = '708779793098084352-Aq59kvjyACqZZwvC7N9Hu8GRpXbNrFM'
access_token_secret = 'DLrNnFWyja1vHhot4FFFinyqR3GCufasHzHBxsHF2ejoc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def order():
	#get most recent dm
	dms = api.direct_messages()
	if dms == []:
	    recent_id = '0' 
	else:
	    recent_id = dms[0].id_str #most recent DM ID

	#uncomment for production
	api.update_status('{} #EasyOrder'.format(target))

	#wait for dominos to send dm.
	#while True:
	#	time.sleep(5)
	#	dms = api.direct_messages(since_id=recent_id) #get most recent DMs
	#	if dms != []: 
	#		if dms[0].sender_screen_name != target: #check if from target
	#			recent_id = dms[0].id_str
	#		else:
	#			break #if from target, go to next step

	#api.send_direct_message(screen_name=target, text='confirm') #CONFIRMED

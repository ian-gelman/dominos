import time
import tweepy

import keys #put your Dominos API keys here. this is .gitignore'd so make this yourself

target = '@dominos'

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth) #log into twitter boi

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

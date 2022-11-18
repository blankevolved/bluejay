import os
import json

bearer_token = ""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

## clears the screen
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def save():
    ## check if save.json dosent exist, if it dosent create it.
    if os.path.exists('save.json') == False:
        with open('save.json', 'w+') as json_file:
            json_file.write('{"bearer_token":"", "consumer_key":"", "consumer_secret":"", "access_token":"", "access_token_secret":""}')
            json_file.close()
    
    ## load the json file with the json module and store it in loaded_json
    with open('save.json', 'r') as json_file:
        loaded_json = json.load(json_file)
        json_file.close()
    
    ## write to the save file
    with open('save.json', 'w+') as json_file:
        loaded_json['bearer_token'] = bearer_token
        loaded_json['consumer_key'] = consumer_key
        loaded_json['consumer_secret'] = consumer_secret
        loaded_json['access_token'] = access_token
        loaded_json['access_token_secret'] = access_token_secret
        json_file.seek(0)
        json.dump(loaded_json, json_file, indent=4)
        json_file.truncate()

        json_file.close()

def load():
    ## check if save.json exists
    if os.path.exists('save.json') == True:
        with open('save.json', 'r') as json_file:
            loaded_json = json.load(json_file)
            global bearer_token
            global consumer_key
            global consumer_secret
            global access_token
            global access_token_secret
            try:
                bearer_token = loaded_json['bearer_token']
                consumer_key = loaded_json['consumer_key']
                consumer_secret = loaded_json['consumer_secret']
                access_token = loaded_json['access_token']
                access_token_secret = loaded_json['access_token_secret']
            except:
                pass    

            json_file.close()

load()

## set tokens if one isnt set
if bearer_token == "" or consumer_key == "" or consumer_secret == "" or access_token == "" or access_token_secret == "":
    bearer_token = input('Bearer Token: ')
    consumer_key = input('Consumer Key: ')
    consumer_secret = input('Consumer Secret: ')
    access_token = input('Access Token: ')
    access_token_secret = input('Access Token Secret: ')
    save()

## import tweepy
try:
    import tweepy as tp
except ImportError:
    os.system('cmd /k "pip install tweepy"')
    clear()
    import tweepy as tp

## def client with tokens
client = tp.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

## Manage Tweets
class Manage_Tweets:
    clear()
    def create_tweet(text: str):
        try:
            client.create_tweet(text=text)
            clear()
            print(f'Tweeted "{text}"')
        except tp.TweepyException as e:
            print(f'ERROR: \n{e}')

## Likes
class Likes:
    clear()
    def like(tweet_id):
        try:
            client.like(tweet_id=tweet_id)
            clear()
            print(f'Liked Tweet: {tweet_id}')
        except tp.TweepyException as e:
            print(f'ERROR: \n{e}')
    def unlike(tweet_id):
        try:
            client.unlike(tweet_id=tweet_id)
            clear()
            print(f'unliked Tweet: {tweet_id}')
        except tp.TweepyException as e:
            print(f'ERROR: \n{e}')
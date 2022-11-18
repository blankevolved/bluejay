## imports
from commands import clear, Manage_Tweets as mt, Likes as l

opts = {
    'help':{
        'cmd':'help',
        'desc':'Shows all cmds',
        'args':[None]
    },
    'tweet':{
        'cmd':'tweet',
        'desc':'Send a tweet!',
        'args':['Tweet Text: str']
        },
    'like':{
        'cmd':'like',
        'desc':'Like a tweet!',
        'args':['Tweet ID: int']
    },
    'unlike':{
        'cmd':'unlike',
        'desc':'Remove a like from a tweet!',
        'args':['Tweet ID: int']
    }
    }

clear()
## main loop
def main():
    print('Type "help" to get a list of commands')
    inp = input('>>> ')
    clear()

    ## options
    if inp == opts['help']['cmd']:
        for i in opts:
            print(f'{opts[i]["cmd"].capitalize()}:')
            print(f'\tDesc:')
            print(f'\t\t{opts[i]["desc"]}')
            print(f'\tArgs:')   
            for a in opts[i]['args']:
                print(f'\t\t{a}')
            print()
    ## manage tweets
    if inp == opts['tweet']['cmd']:
        tweet_text = input('Tweet Text: ')
        mt.create_tweet(tweet_text)
    ## likes
    if inp == opts['like']['cmd']:
        tweet_id = input('Tweet ID: ')
        l.like(tweet_id)
    
    if inp == opts['unlike']:
        tweet_id = input('Tweet ID: ')
        l.unlike(tweet_id)


while True:
    main()
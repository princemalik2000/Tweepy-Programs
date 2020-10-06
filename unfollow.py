import time
import tweepy
import config

#unfollow specific user
try:
    api.destroy_friendship(enemy)
except:
    pass

#unfollow people who don't follow back
def newunfollow():
    unfrndlist = []
    for user in tweepy.Cursor(api.friends, screen_name='yourusername').items():
        john = user.screen_name
        try:
            frndstatus = api.show_friendship(source_screen_name=john, target_screen_name='yourusername')
            time.sleep(10)
            if frndstatus[0].following is True:
                pass
            elif frndstatus[0].following is False:
                unfrndlist.append(john)
            else:
                pass
        except:
            pass
    time.sleep(100)
    for i in range(0, len(unfrndlist)):
        try:
            api.destroy_friendship(unfrndlist[i])
        except:
            pass
        time.sleep(20)

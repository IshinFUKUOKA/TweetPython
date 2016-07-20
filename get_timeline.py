# -*- coding: utf-8 -*-
import datetime
import time

if __name__ == '__main__':
    import twpy
    api = twpy.api
    last_tweet_id = None
    while(True):
        if(last_tweet_id == None):
            print("Get Recent Tweet")
            recent_tl = api.home_timeline(count=200)
        else:
            print("Get Recent Tweet since %s" % last_tweet_id)
            recent_tl = api.home_timeline(since_id=int(last_tweet_id),count=200)
        print("%s tweets are loaded." % len(recent_tl))
        for tweet in recent_tl:
            with open('tweet.txt', 'a') as fp:
                tweet_id = str(tweet.id)
                tweeted_at = str(tweet.created_at + datetime.timedelta(hours=9))
                user_name = tweet.user.name
                tweet_text = tweet.text
                text = u'\t'.join(['[Tweet]',tweet_id, tweeted_at, user_name, tweet_text])
                fp.write(text.encode('utf-8'))
                fp.write('\n')
                if (last_tweet_id == None or last_tweet_id < tweet.id):
                    last_tweet_id = tweet_id
                    print("last_tweet_id is %s" % tweet.id)
        print("Success")
        time.sleep(60)

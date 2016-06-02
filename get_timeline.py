# -*- coding: utf-8 -*-
import datetime

if __name__ == '__main__':
    import twpy
    api = twpy.api
    recent_tl = api.home_timeline(count=200)
    for tweet in recent_tl:
        with open('tweet.txt', 'a') as fp:
            tweet_id = str(tweet.id)
            tweeted_at = str(tweet.created_at + datetime.timedelta(hours=9))
            user_name = tweet.user.name
            tweet_text = tweet.text
            text = u'\t'.join(['[Tweet]',tweet_id, tweeted_at, user_name, tweet_text])
            fp.write(text.encode('utf-8'))
            fp.write('\n')

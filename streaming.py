# -*- coding: utf-8 -*-
 
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import ConfigParser
import json

inifile = ConfigParser.SafeConfigParser()
inifile.read('config.ini')
 
consumer_key = inifile.get('user', 'consumer_key')
consumer_secret = inifile.get('user', 'consumer_secret')
access_token = inifile.get('user', 'access_token')
access_token_secret = inifile.get('user', 'access_token_secret')
 
class StdOutListener(StreamListener):
    def on_data(self, data):
        if data.startswith("{"):
            print data.rstrip()
        return True
 
    def on_error(self, status):
        print status
 
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 
    stream = Stream(auth, l)
    # stream.filter(track = [keyword])#検索する場合
    # stream.sample()#ツイートのランダムサンプリングを取得する場合
    # stream.userstream()#タイムラインを取得する場合

# 自動bot 

import tweepy
import time

# Twitter APIキーとシークレットを設定
consumer_key = '4vBBCBF9ywhKCDgaHTPkQ1e0v'
consumer_secret = 'J54kLldJe9ur2iF5GuxyBESOxpoODCKQ2U59hiO02kjBfKubTU'
access_token = '1496353791314391042-Pyl2xSoLN11e8vKYHbLiMLsVqCrpqO'
access_token_secret = 'GxXtYxrrf9XIk9Dx3hfznDgfi8LLLHpzFjQ6mzApi8hLg'

# Tweepyの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# ツイートの内容リスト
tweets = [
    "Hello, world! This is automated tweet 1.",
    "Hello, world! This is automated tweet 2.",
    "Hello, world! This is automated tweet 3."
]

# 一定時間ごとにツイートを投稿
for tweet in tweets:
    api.update_status(tweet)
    print(f"Tweeted: {tweet}")
    time.sleep(10)  # 10秒ごとにツイートを投稿

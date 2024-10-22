# 特定語句自動リポスト

import tweepy

# Twitter APIの認証情報を設定
API_KEY = '4vBBCBF9ywhKCDgaHTPkQ1e0v'
API_SECRET_KEY = 'J54kLldJe9ur2iF5GuxyBESOxpoODCKQ2U59hiO02kjBfKubTU'
ACCESS_TOKEN = '1496353791314391042-Pyl2xSoLN11e8vKYHbLiMLsVqCrpqO'
ACCESS_TOKEN_SECRET = 'GxXtYxrrf9XIk9Dx3hfznDgfi8LLLHpzFjQ6mzApi8hLg'
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHgtwgEAAAAAEsJhU0MJYVlGswHHYqyMcHZwpr8%3DhoPXaMJuzbYtdbz9rU84VtEYs39tTRprzrTzfyY50IpzzRC2RW"

# 認証
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_SECRET_KEY, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

# 東京周辺の緯度経度の範囲（ボックス範囲）
TOKYO_AREA = [139.559, 35.529, 139.913, 35.856]  # 経度、緯度の最小値と最大値


# StreamingClientを使って特定のツイートをリツイートする
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"New tweet found: {tweet.text}")
        
        # リツイートの条件（例：特定のキーワードが含まれている）
        if "Python" in tweet.text:
            try:
                # リツイートする
                client.retweet(tweet.id)
                print(f"Retweeted: {tweet.id}")
            except Exception as e:
                print(f"Error: {e}")

# ストリーミングクライアントを作成
stream = MyStream(BEARER_TOKEN)

# ストリームルールを設定（"Python" というキーワードを追跡）
stream.add_rules(tweepy.StreamRule("大谷翔平"))

# ストリームを開始
stream.filter(track=['大谷翔平'], locations=TOKYO_AREA)

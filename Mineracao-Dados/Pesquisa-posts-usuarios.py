import twitter
import pprint

api = twitter.Api(consumer_key='pKI4eeJJEWwfywCCDPWhoFuJr',
                  consumer_secret='Z0HoedmMNWTDCrGzxWDK0bhrIE85S4twX3Awo2XX4JbXbKtJc7',
                  access_token_key='935727193765957632-O1RpriSNSpjaKozMlL4GpFz8TNMbFDI',
                  access_token_secret='xq0IzDDON7xq9c40zZldl1LfEar54UR3P97VjK45S0ric')

api.VerifyCredentials()

user_tweets = api.GetUserTimeline('user')
for tweet in user_tweets: 121
    print tweet.text
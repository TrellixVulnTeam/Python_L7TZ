#!/usr/env python
# -*- coding: utf-8 -*-
import twitter
import pprint

api = twitter.Api(consumer_key='pKI4eeJJEWwfywCCDPWhoFuJr',
                  consumer_secret='Z0HoedmMNWTDCrGzxWDK0bhrIE85S4twX3Awo2XX4JbXbKtJc7',
                  access_token_key='935727193765957632-O1RpriSNSpjaKozMlL4GpFz8TNMbFDI',
                  access_token_secret='xq0IzDDON7xq9c40zZldl1LfEar54UR3P97VjK45S0ric')

api.VerifyCredentials()
# <twitter.user.User object at 0x02EE5EF0>

status_list = api.GetSearch(
    geocode=None, term='Gatinha', since_id = None,
                                             lang ='pt', count = 10, result_type ='recent'
)

print(status_list)
# [<twitter.status.Status object at 0x03078AF0>, <twitter.status.Status object at 0x03078B90>, <twitter.status.Status object at 0x03078C50>, <twitter.status.Status object at 0x03078D30>, <twitter.status.Status object at 0x03078D90>, <twitter.status.Status object at 0x03078DF0>, <twitter.status.Status object at 0x03078E50>, <twitter.status.Status object at 0x03078F10>, <twitter.status.Status object at 0x03078F70>, <twitter.status.Status object at 0x03088030>]

help(twitter.Status)

status_list[0].GetText()
# u’RT @PandaRcds: @edmilsonpapo10 @OThereza MAIS UMA DAS MENTIRAS DO LULA LADR\xc3O DO BRASIL!’

hashtags = dict()

for status in status_list:
    status_hashtags = status.hashtags
    for hash in status_hashtags:
        if hashtags.get(hash.text) is None:
            hashtags[hash] = 1
        else:
            hashtags[hash] += 1

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(hashtags)
import facebook
import requests
from prettytable import PrettyTable
from collections import Counter



def some_action(post):
    print post['name']


access_token = '' ## Insert access-token here

g = facebook.GraphAPI(access_token)

friends = g.get_connections("me", "friends")['data']
likes = { friend['name'] : g.get_connections(friend['id'], "likes")['data']
for friend in friends }



friends_likes = Counter([like['name']
for friend in likes
    for like in likes[friend]
        if like.get('name')])


pt = PrettyTable(field_names=['Name', 'Freq'])
pt.align['Name'], pt.align['Freq'] = 'l', 'r'
[ pt.add_row(fl) for fl in friends_likes.most_common(10) ]

print 'Top 10 likes amongst friends'
print pt


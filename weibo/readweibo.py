import json
import codecs
import ast

f = open("weibo-content.txt")
data = f.read()

d=ast.literal_eval(data)
print(type(d))
statuses=d['statuses']
print(len(statuses))

#js = json.loads(data)
#print(json.dumps(js, indent=4))

for i in range(0, len(statuses)):
    print('==============================================')
    print('微博创建时间:', statuses[i]['created_at'])
    print('昵称:', statuses[i]['user']['screen_name'])
    print('简介:', statuses[i]['user']['description'])
    print('位置:', statuses[i]['user']['location'])
    print('微博:', statuses[i]['text'])
    #print u"微博创建时间:" + statuses[i]['created_at']
    #print u'昵称:' + statuses[i]['user']['screen_name']
    #print u'简介:' + statuses[i]['user']['description']
    #print u'位置:' + statuses[i]['user']['location']
    #print u'微博:' + statuses[i]['text'
f.close()

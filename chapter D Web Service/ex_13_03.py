import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json


sum=0

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    #if api_key is not False: parms['key'] = api_key
    #url = serviceurl + urllib.parse.urlencode(parms)
    #url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    #tree = ET.fromstring(data)
    info = json.loads(data)
    print('User count:', len(info['comments']))

    for item in info['comments']:
        #print('Name', item['name'])
        sum = sum + int(item['count'])
        #print('Attribute', item['x'])
    print('sum is ',sum)
    sum=0

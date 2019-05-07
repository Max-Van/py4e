import webbrowser
import sinaweibopy3
import urllib.request, urllib.parse, urllib.error
import json
import ssl


def main():
    '''
    if you want to use this api,you should follow steps follows to operate.
    '''
    try:
        # step 1 : sign a app in weibo and then define const app key,app srcret,redirect_url
        APP_KEY = '1155879251'
        APP_SECRET = '213be2d9be87877f9f755bd6899eea5c'
        REDIRECT_URL = 'http://api.weibo.com/oauth2/default.html'
        # step 2 : get authorize url and code
        client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
        url = client.get_authorize_url()
        # print(url)
        webbrowser.open_new(url)
        # step 3 : get Access Token
        # Copy the above address to the browser to run,
        #enter the account and password to authorize, the new URL contains code
        result = client.request_access_token(
            input("please input code : "))  # Enter the CODE obtained in the authorized address
        print(result)
        # At this point, the access_token and expires_in should be saved,
        # because there is a validity period.A
        # If you need to send the microblog multiple times in a short time,
        # you can use it repeatedly without having to acquire it every time.
        client.set_access_token(result.access_token, result.expires_in)

        # step 4 : using api by access_token
        #print(client.public_timeline())  # get the latest public Weibo

        #f = open("weibo-content.txt", "w")
        #f.write( str(client.public_timeline())  )      # str() converts to string
        #f.close()
        data = str(client.public_timeline())
        js = json.loads(data)
        print(json.dumps(js, indent=4))



        # =============================================================================
        #         statuses = client.public_timeline()['statuses']
        #         length = len(statuses)
        #         for i in range(0,length):
        #             print("昵称："+statuses[i]['user']['screen_name'])
        #             print("简介："+statuses[i]['user']['description'])
        #             print("位置："+statuses[i]['user']['location'])
        # =============================================================================
        '''
        in this step,the api name have to turn '/' in to '__'
        for example,statuses/public_timeline(this is a standard api name) have to turn into statuses__public_timeline
        '''
        # Or use this method
        #print(client.get.statuses__public_timeline())
        #data = client.get.statuses__public_timeline()
        #print(client.get.users__show())

        #js = json.loads(data)
        #print(json.dumps(js, indent=4))
        #statuses = client.statuses__public_timeline()
        #length = len(statuses)
        # 输出了部分信息
        #for i in range(0, length):
        #    print ('微博创建时间', statuses[i]['created_at'])

    #print u"微博创建时间:" + statuses[i]['created_at']
    #print u'昵称:' + statuses[i]['user']['screen_name']
    #print u'简介:' + statuses[i]['user']['description']
    #print u'位置:' + statuses[i]['user']['location']
    #print u'微博:' + statuses[i]['text'



        # Obtain the UID of the authorized user
        #print(client.get.account__get_uid())

    except ValueError:
        print('pyOauth2Error')

if __name__ == '__main__':
    main()

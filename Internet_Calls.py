#AUTHOR: Jason Abrams

import urllib.request, json, urllib.error
import random

from my_info import Information

class API_Calls:

    def __init__(self):
        super().__init__()
        self.Giphy_Data = {}
        self.INFO = Information()
        self.Giphy_Key = self.INFO.Get_Giphy_TOKEN()

    def Giphy_API_Call(self, item: str, limit: str, type :int):

        item = item.replace(" ", "+")

        uri = "http://api.giphy.com/v1/gifs/search?q=" + item + "&api_key=" + self.Giphy_Key + "&limit=" + limit 
        
        try:
            with urllib.request.urlopen(uri) as URL:
                data = json.loads(URL.read().decode())
                self.Giphy_Data = data

                d = data['data']

                #Returns an address for the url
                URL.close()

                #Returns the raw url that Discord can use
                if(type == 0):
                    return random.choice(d)['url']
                #returns the media link to use the gif with an embed
                elif(type == 1):
                    link = "https://media.giphy.com/media/{0}/giphy.gif".format(random.choice(d)['id'])
                    return link
                #else returns None because it needs a type
                else:
                    return None
        
        except urllib.error.HTTPError:
            print("Sorry, HTTP")
            return None

        except:
            print("Sorry, something else")
            return None

    def Speedrun_API_Call(self):
        pass

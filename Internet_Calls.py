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

    def Giphy_API_Call(self, item: str, limit: str):

        item = item.replace(" ", "+")

        uri = "http://api.giphy.com/v1/gifs/search?q=" + item + "&api_key=" + self.Giphy_Key + "&limit=" + limit 
        
        try:
            with urllib.request.urlopen(uri) as URL:
                data = json.loads(URL.read().decode())
                self.Giphy_Data = data

                d = data['data']

                #Returns an address for the url
                URL.close()
                return random.choice(d)['url']
        
        except urllib.error.HTTPError:
            print("Sorry, HTTP")
            return None

        except:
            print("Sorry, something else")
            return None
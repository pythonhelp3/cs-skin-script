import requests
import base64
from config import clientId, clientSecret




# This is slowing being worked on .. I will only allows for easier price managementabs
# The objective is to simplify the process of adding and removing items from the cart


# Update: Soon will provide an interface for search historical features of the skinport database
#           such as item prices, quantities market item names, trade statues, stock details, sales feed,
#           and account history

# https://api.skinport.com/v1/account/transactions?page=1&limit=100&order=desc

class Client:

    def __init__(self, url, api, api_secret):
        self.base_url = url
        self.clientId = api
        self.clientSecret = api_secret

    def auth(self):

        self.clientData = f"{self.clientId}:{self.clientSecret}"
        self.encodedData = str(base64.b64encode(self.clientData.encode("utf-8")), "utf-8")
        self.authorizationHeaderString = f"Basic {self.encodedData}"
    
    def get_data(self):
        pass

    




# simple client call
client = Client('https://api.skinport.com/', clientId, clientSecret)



# test response from API
r = requests.get('https://api.skinport.com/v1/items', params={
    "app_id": 730,
    "currency": "USD",
    "tradable": 0}).json()

print(r)
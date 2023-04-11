import requests
import base64
from config import api_key_clientId, api_key_clientSecret




# This is slowing being worked on .. I will only allows for easier price managementabs
# The objective is to simplify the process of adding and removing items from the cart


# Update: Soon will provide an interface for search historical features of the skinport database
#           such as item prices, quantities market item names, trade statues, stock details, sales feed,
#           and account history

# https://api.skinport.com/v1/account/transactions?page=1&limit=100&order=desc

class Client:

    def __init__(self, url):
        self.base_url = url
        self.clientId = api_key_clientId
        self.clientSecret = api_secret_clientSecret

    def auth(self):
        self.clientData = f"{self.clientId}:{self.clientSecret}"
        self.encodedData = str(base64.b64encode(self.clientData.encode("utf-8")), "utf-8")
        self.authorizationHeaderString = f"Basic {self.encodedData}"
    
    def get_item_orderbook(self, currency, tradable = 0, app_id = "730"):
        r = requests.get("https://api.skinport.com/v1/items", params={
            "app_id": app_id,
            "currency": currency,
            "tradable": 0
        }).json()


    # # Getters to add:
    # def get_sales_history(self, name, currency, app_id = "730"):
    #     pass
    # def check_stock(self, name, currency):
    #     pass
    # def get_transactions(self, limit, order)

    
# simple client call
client = Client('https://api.skinport.com/', api_key_clientId, api_key_clientSecret)
item_orders = client.get_item_orderbook("USD")
print(item_orders)


import requests

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# This will allow the user to save their config file in the user directory
# instead of the current directory by adding a config.yaml file


# Create a class object to hold the API key and secret
class API:
    def __init__(self, api_key, api_secret, user):
        self.api_key = api_key
        self.api_secret = api_secret
        self.user = user

    def get_api_key(self):
        return self.api_key

    def get_api_secret(self):
        return self.api_secret


api = API(api_key=api_key, api_secret=api_secret)





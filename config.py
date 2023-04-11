import os

# Define the file name and location for the config file
config_file = "config.txt"
config_path = os.path.abspath(config_file)

# Check if the config file exists
if os.path.isfile(config_path):
    # If the file exists, read it and store the values in variables
    with open(config_path, "r") as f:
        api_key_clientId = f.readline().strip()
        api_key_clientSecret = f.readline().strip()
else:
    # If the file does not exist, create it and ask for API keys
    api_key_clientId = input("Enter ClientId API Key: ")
    api_key_clientSecret = input("Enter ClientSecret API Key: ")
    with open(config_path, "w") as f:
        f.write(api_key_clientId + "\n")
        f.write(api_key_clientSecret + "\n")

# Use the API keys in your program as needed
print("ClientId API Key:", api_key_clientId)
print("ClientSecret API Key:", api_key_clientSecret)

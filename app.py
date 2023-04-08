from skinportassistbot import Bot
from api import Client
import typer
from . import config

# (Camden comment): Here is the link to the API on Skinport's website, I'm not sure how it's used or if it will work for this use application. If not, it could be a useful
# tool for calculating profit if the item is relisted on each item since items under $1000 have a sales fee of 12% and items over $1000 have a sales fee of 6%.

# Link: https://docs.skinport.com

def main() -> None:
    api_key = config.get("clientId")
    api_secret = config.get("clientSecret")

    client = Client(api_key, api_secret)

    

def entry_point() -> None:
    typer.run(main)

if __name__ == "__main__":
    entry_point()
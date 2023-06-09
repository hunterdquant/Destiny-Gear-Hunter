### tutorial from https://www.youtube.com/watch?v=IcES0K5VCns&ab_channel=TekkSparrowPrograms%21 

from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://hunterdquant.github.io/Destiny-Gear-Hunter/"
token_url = "https://www.bungie.net/Platform/App/OAuth/token/"

get_user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url,state=None)


auth_link = session.authorization_url(base_auth_url)
print(f"Authlink: {auth_link[0]}")

redirect_response = input("Paste your redirect url with query params here: ")

session.fetch_token(client_id=client_id,
                    client_secret=client_secret,
                    token_url=token_url,
                    authorization_response=redirect_response)

additional_headers = {'X-API-KEY': api_key}
response = session.get(url=get_user_details_endpoint, headers=additional_headers)

print(f"Response status: {response.status_code}")
print(f"Response status: {response.reason}")
print(f"Response text: \n{response.text}")
import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._endpoint = os.environ["SHEETY_PRICES_ENDPOIT"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._endpoint, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

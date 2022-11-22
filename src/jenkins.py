import requests

import constants
from config import Config


class Jenkins:
    def __init__(self):
        self.constants = constants
        self.config = Config()

    def build_url(self, job: str) -> str:
        return f"{self.config.get_api_url()}/{job['view']}/job/{job['name']}/lastSuccessfulBuild/api/json"

    def get_last_timestamp(self, job: str) -> str:
        url = self.build_url(job)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()["timestamp"]

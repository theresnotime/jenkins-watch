import requests

from config import Config


class Jenkins:
    def __init__(self):
        self.config = Config()

    def build_url(self, job):
        return f"{self.config.get_api_url()}/{job['view']}/job/{job['name']}/lastSuccessfulBuild/api/json"

    def get_last_timestamp(self, job):
        url = self.build_url(job)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()["timestamp"]

import json
import os

import constants


class Config:
    def __init__(self):
        self.constants = constants
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json"),
            "rb",
        ) as read_file:
            self.config = json.load(read_file)

    def get(self, key: str) -> str:
        return self.config[key]

    def get_job(self, job: str) -> str:
        return self.get("jobs")[job]

    def get_api_url(self) -> str:
        return self.config["api"]["url"]

    def setup_confirms(self) -> dict:
        confirms = {}
        for job in self.get("jobs").values():
            confirms[job["name"]] = 0
        return confirms

    def setup_alerted(self) -> dict:
        alerted = {}
        for job in self.get("jobs").values():
            alerted[job["name"]] = False
        return alerted

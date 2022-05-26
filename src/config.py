import json
import os


class Config:
    def __init__(self):
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json"),
            "rb",
        ) as read_file:
            self.config = json.load(read_file)

    def get(self, key):
        return self.config[key]

    def get_job(self, job):
        return self.get("jobs")[job]

    def get_api_url(self):
        return self.config["api"]["url"]

    def setup_vars(self):
        confirms = {}
        for job in self.get("jobs").values():
            confirms[job["name"]] = 0
        return confirms

import requests

import constants
from config import Config


class Alert:
    def __init__(self):
        self.constants = constants
        self.config = Config()

    def send_alert(self, alert: str, job: str) -> None:
        if self.config.get("debug"):
            print(f"Sending {alert} alert for {job}")

        if alert == "pushover":
            url = self.config.get("alerts")["pushover"]["url"]
            params = {
                "title": f"{job} is overdue",
                "token": self.config.get("alerts")["pushover"]["token"],
                "user": self.config.get("alerts")["pushover"]["user"],
                "message": f"{job} is overdue",
                "url": self.config.get_job(job)["url"],
                "device": self.config.get_job(job)["alerts"]["pushover"]["device"],
                "priority": self.config.get_job(job)["alerts"]["pushover"]["priority"],
            }
            requests.post(url, data=params)

    def do_alert(self, job: str) -> None:
        job_alerts = self.config.get_job(job)["alerts"]
        if job_alerts:
            for alert in job_alerts.keys():
                self.send_alert(alert, job)
        return

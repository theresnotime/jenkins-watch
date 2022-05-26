import time
from datetime import datetime

from alert import Alert
from config import Config
from jenkins import Jenkins


def do_sleep():
    if config.get("debug"):
        print(f"Sleeping for {config.get('interval')}s")
    time.sleep(config.get("interval"))


def main():
    confirm_count = config.setup_vars()
    run_check = True

    while run_check:
        for job in config.get("jobs").values():
            timestamp = jenkins.get_last_timestamp(job)
            last_built = datetime.fromtimestamp(int(timestamp) / 1000)
            time_delta = round((datetime.now() - last_built).total_seconds())
            job_overdue = job["overdue"]
            if time_delta > job_overdue:
                confirm_count[job["name"]] += 1
                if confirm_count[job["name"]] >= job["confirms"]:
                    print(f"{job['name']} is overdue")
                    alert.do_alert(job["name"])
            else:
                confirm_count[job["name"]] = 0

            if config.get("debug"):
                print(
                    f"Job \"{job['name']}\" lastSuccessfulBuild = {last_built}. ({time_delta}s ago) - will alert if > {job_overdue}s and {confirm_count[job['name']]} >= {job['confirms']}"
                )

        do_sleep()


if __name__ == "__main__":
    config = Config()
    jenkins = Jenkins()
    alert = Alert()

    print(f"Jenkins watch {config.get('version')} started")
    if config.get("debug"):
        print("Debugging..")
    main()

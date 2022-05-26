# Jenkins Watch
[![Python](https://github.com/theresnotime/jenkins-watch/actions/workflows/python.yml/badge.svg)](https://github.com/theresnotime/jenkins-watch/actions/workflows/python.yml) [![CodeQL](https://github.com/theresnotime/jenkins-watch/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/theresnotime/jenkins-watch/actions/workflows/codeql-analysis.yml)

*Jenkins Watch* is a Python script which monitors the `lastSuccessfulBuild` timestamp of a job and sends a notification when the job is considered overdue.

## Configuration
The configuration is done in the `config.json` file.

```json
{
    "debug": false, // Set to true to enable debug messages
    "interval": 60, // How often to check the jobs (in seconds)
    "api": {
        "url": "https://jenkins.api.url" // The Jenkins API URL
    },
    "alerts":{
        "pushover": {
            "enabled": true,
            "url": "https://api.pushover.net/1/messages.json",
            "token": "application_token", // Pushover application token
            "user": "user_token" // Pushover user token
        }
    },
    "jobs": {
        "job-name": { // The job name in Jenkins
            "name": "job-name", // The job name in Jenkins
            "url": "https://link.to.jenkins.job/", // A link to the Jenkins job
            "view": "jenkins-view", // The "view" the job is in
            "overdue": 1500, // After how many seconds the job is considered overdue
            "confirms": 2, // How many times the job has to be reported overdue before sending a notification
            "alerts": {
                "pushover": {
                    "device": "device_name", // Pushover device name
                    "priority": 0 // Default priority
                }
            }
        },
        "job-with-no-alert": {
            "name": "job-with-no-alert",
            "url": "https://link.to.jenkins.job/",
            "view": "jenkins-view",
            "overdue": 1500,
            "confirms": 2,
            "alerts": [] // Leaving this empty disables notifications
        }
    }
}
```
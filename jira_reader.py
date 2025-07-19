import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

def get_jira_ticket_details(issue_id):
    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{issue_id}"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, auth=auth)
    
    if response.status_code != 200:
        raise Exception(f"Jira API error: {response.status_code} - {response.text}")

    issue = response.json()
    title = issue['fields']['summary']
    description = issue['fields']['description']['content'][0]['content'][0]['text']

    return title, description
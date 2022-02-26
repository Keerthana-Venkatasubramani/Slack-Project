import slack
import os
from pathlib import Path
from dotenv import load_dotenv
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
client=slack.WebClient(token=os.getenv("SLACK_TOKEN"))
request = client.api_call("users.list")
if request['ok']:
    for user in request['members']:  
        if user['is_bot'] == False and user['id'] != 'USLACKBOT':
            print(user['real_name'])    
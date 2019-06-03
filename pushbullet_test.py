# Developed by Vishal Keshav
# Net Puppy version 0.01

import os
import subprocess
import time

import requests
from websocket import create_connection
from requests.auth import HTTPBasicAuth
import json

def get_notification(data, token):
    # Limit the push messeges to just 1 (the latest one)
    url = "https://api.pushbullet.com/v2/pushes?limit=1"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "User-Agent": "pyPushBullet"}
    r = requests.request("GET", url, data=None, params=None, headers=headers,
                                    files=None, auth=HTTPBasicAuth(token, ""))
    r.raise_for_status()
    return r.json()

def run_command(command_str):
    if command_str[0] == 'C':
        os.system(command_str[2:])
    else:
        print("invalid command, " + command_str)


def realtime(token):
    url = "wss://stream.pushbullet.com/websocket/" + token
    ws = create_connection(url)
    while 1:
        # sleep for some time if we dont want nops too much
        # nr_seconds = 60 # Sleep for 1 minutes
        #time.sleep(nr_seconds)
        data = ws.recv()
        data = json.loads(data)
        if data["type"] != "nop":
            if data["type"] == "tickle":
                notification = get_notification(data, token)
                run_command(notification['pushes'][0]['body'])

#-------------------------------------TEST--------------------------------------
def main():
    while 1:
        print("Do something")
        time.sleep(2)

if __name__ == "__main__":
    token = ""
    realtime(token)

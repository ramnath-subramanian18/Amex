import requests
import os
from dotenv import load_dotenv

def send_log_to_loggly(token, data):
    url = f"https://logs-01.loggly.com/inputs/{token}/tag/http/"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Log sent successfully")
    else:
        print(f"Failed to send log. Status code: {response.status_code}")
        print("Response:", response.text)
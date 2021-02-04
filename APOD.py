import json
import time
import requests
import random
from time import sleep
import schedule


# Your Discord webhook settings.
webhook_url = "Enter your webhook url"
nasa_api_key = "Enter the NASA api key"


def apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
    response = requests.get(url)
    res = response.json()   
    if len(res["explanation"]) > 1024:
        embed = {"image": {"url": res["url"]}, "color": random.randint(0, 0xffffff),
                 "fields": [{"name": "Astronomy Photo Of The Day:", "value": res["title"]},
                            {"name": "Date:", "value": res["date"]},
                            {"name": "Explanation:",
                             "value": "The explanation can't be depicted since the character length exceeds the 1024 character limit. Please refer to: https://apod.nasa.gov/apod/archivepix.html for further information."}]}
    else:
        embed = {"image": {"url": res["url"]}, "color": random.randint(0, 0xffffff),
                 "fields": [{"name": "Astronomy Photo Of The Day:", "value": res["title"]},
                            {"name": "Date:", "value": res["date"]},
                            {"name": "Explanation:", "value": res["explanation"]}]}
    data = {"embeds": [embed]}
    requests.post(webhook_url, json=data)
    print("A new astronomy photo has arrived.")

schedule.every().day.at("11:00").do(apod)


while True:
    schedule.run_pending()
    time.sleep(1)

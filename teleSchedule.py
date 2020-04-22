# BOT MADE TO SEND SCHEDULED MESSAGES
# Uses 'ids.txt' to get user ids of those who have used the bot.File created automatically with main.py

import schedule
import requests
import urllib.parse

import os

import time
from datetime import date
from datetime import datetime

from getInformation import rootnetCountry
from getInformation import rootnetState
from getInformation import get_stats_total

# PRECAUTIONS FOR DEPLOYING
# os.environ["TZ"] = "Asia/Kolkata"
# time.tzset()

with open("Token",'r') as f:
    BOTTOKEN=f.readline()

def sendMessage(id,MESSAGE):
    id=str(id)
    url='https://api.telegram.org/bot'+BOTTOKEN+'/sendMessage?chat_id='
    requests.get(url+id+'&text='+urllib.parse.quote(MESSAGE))

def broadcast():
    today = datetime.today()
    print(today.strftime("%Y-%m-%d %H:%M:%S"))
    print('Broadcasting....')
    total=get_stats_total()
    today = date.today()
    mData=rootnetCountry()
    MESSAGE=today.strftime("%B %d, %Y")+'\n\nTotal number of COVID-19 Cases in India : '+str(total)+"\nNumber of Cured cases : "+str(mData[1])+"\nNumber of Deaths : "+str(mData[2])+"\n\nData sources : covid19india.org & api.rootnet.in""\n\nStay Safe."
    with open('ids.txt','r') as f:
        data=f.read()
    data=data.split('\n')
    for id in data:
        if id=='':
            continue
        sendMessage(id,MESSAGE)

# SCHEDULED PROCESSES
schedule.every().day.at("08:00").do(broadcast)
schedule.every().day.at("12:00").do(broadcast)
schedule.every().day.at("16:00").do(broadcast)
schedule.every().day.at("19:51").do(broadcast)
schedule.every().day.at("23:59").do(broadcast)

while True:
    schedule.run_pending()
    time.sleep(1)

import schedule
import requests
import time
import urllib.parse
from datetime import date
import os
from datetime import datetime
from source2 import mAllInfo
from source2 import mStateInfo
from getInformation import get_stats_total
# os.environ["TZ"] = "Asia/Kolkata"
# time.tzset()

# SET BOT TOKEN HERE
BOTTOKEN=''

def sendMessage(id,MESSAGE):
    id=str(id)
    url='https://api.telegram.org/bot'+BOTTOKEN
    requests.get(url+id+'&text='+urllib.parse.quote(MESSAGE))

def broadcast():
    today = datetime.today()
    print(today.strftime("%Y-%m-%d %H:%M:%S"))
    print('Broadcasting....')
    total=get_stats_total()
    today = date.today()
    mData=mAllInfo()
    MESSAGE=today.strftime("%B %d, %Y")+'\n\nTotal number of COVID-19 Cases in India : '+str(total)+"\nNumber of Cured cases : "+str(mData[1])+"\nNumber of Deaths : "+str(mData[2])+"\n\nData sources : covid19india.org & api.rootnet.in""\n\nStay Safe."
    with open('testIDS.txt','r') as f:
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
schedule.every().day.at("20:00").do(broadcast)
schedule.every().day.at("23:59").do(broadcast)

while True:
    schedule.run_pending()
    time.sleep(1)

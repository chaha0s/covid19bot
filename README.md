# covid19bot
A telegram bot using Data from covid19india.org to send scheduled messages.

Uses [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)
Install it with *pip install python-telegram-bot*

Before running
*Set BOTTOKEN in Token file.*

<img src="/covid19india.jpeg?raw=true" width="240" title="COVID19IND1A_BOT"></img>
## Bot Features
- Sends scheduled messages
- Send Number of total patients in districts of any state
- Compare data from covid19india and mohfw


###### main.py 
- The main file.Keep it runing for the bot to be able to respond.
- It has predefined keyboard with all Indian States and return number of Total COVID-19 cases, Cured cases and deaths in that particular region.
- It also sends district wise breakup of active cases in particular state.

###### teleSchedule.py
- Uses Scheduler to send timed messages about total COVID-19 Cases in India.

###### getInformation.py
- To get information from 3 sources. 
1)[COVID19INDAI.org](https://api.covid19india.org)
2)[MOHFW](https://www.mohfw.gov.in)
3)[ROOTNET.in](https://api.rootnet.in)


>Lockdown period. 
Could see many people receiving and spreading fake news items everywhere. 
Had nothing to do and came across covid19india.org 's API.Tried to make a telegram bot to send verified information.
Link to the bot: http://t.me/COVID19IND1A_BOT

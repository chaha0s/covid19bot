# covid19bot
A telegram bot using Data from covid19india.org to send scheduled messages.

Uses [Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot)
Install it with *pip install python-telegram-bot*

Before running
*Set BOTTOKEN in each file before using it.*
*Make a blank .txt file "ids.txt" in the same directory.*

###### main.py 
- The main file.Keep it runing for the bot to be able to respond.
- It has predefined keyboard with all Indian States and return number of Total COVID-19 cases, Cured cases and deaths in that particular region.
- It also sends district wise breakup of active cases in particular state.

###### teleSchedule.py
- Uses Scheduler to send timed messages about total COVID-19 Cases in India.

###### compareBot.py
- Compares state data from [covid19india](covid19india.org) and [mohfw.gov.in](mohfw.gov.in)

###### data.py
- To fetch data from [covid19india](covid19india.org) and [mohfw.gov.in](mohfw.gov.in)

###### source2.py
- To get Data from [api.rootnet.in](api.rootnet.in) (cured cases and deaths)

>Lockdown period. 
Could see many people receiving and spreading fake news items everywhere. 
Had nothing to do and came across covid19india.org 's API.Tried to make a telegram bot to send verified information.
Link to the bot: http://t.me/COVID19IND1A_BOT

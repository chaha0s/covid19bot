import requests
import json
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import urllib.parse
from source2 import mAllInfo
from source2 import mStateInfo
from getInformation import get_stats_total

# SET BOT TOKEN HERE
BOTTOKEN=''


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
CHOOSING = range(1)
reply_keyboard = [["India"],["Delhi","Andhra Pradesh"],["Arunachal Pradesh","Assam"],["Bihar","Chhattisgarh"],["Goa","Gujarat"],["Haryana","Himachal Pradesh"],["Jharkhand","Karnataka"],["Kerala","Madhya Pradesh"],["Maharashtra","Manipur"],["Mizoram","Odisha"],["Punjab","Rajasthan"],["Tamil Nadu","Telangana"],["Uttar Pradesh","Uttarakhand"],["West Bengal","Ladakh"],["Jammu and Kashmir","Puducherry"],["Chandigarh","Andaman and Nicobar Islands"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def messageWithPurpose(message,id):
    # Just to store Names of those who use the bot
    id=str(id)
    url='https://api.telegram.org/bot'+BOTTOKEN+'/sendMessage?chat_id='
    send=requests.get(url+id+'&text='+urllib.parse.quote(message))
    response=send.json()
    try:
        with open('msg.txt','a') as f:
            try:
                lname=str(response['result']['chat']['last_name'])
            except:
                lname=''
            f.write(str(response['result']['chat']['id'])+" :: "+str(response['result']['chat']['first_name'])+" "+lname+"\n")
    except:
        pass

def get_state_total(state):
    total=0
    data=requests.get('https://api.covid19india.org/state_district_wise.json')
    data=data.json()
    STATE=''
    dat=[]
    for x,y in data.items():
        for district in y['districtData']:
            if x==state:
                STATE=STATE+district+" : " + str(data[x]['districtData'][district]['confirmed']) +"\n"
                Number=(data[x]['districtData'][district]['confirmed'])
                total=total+Number
    dat.append(STATE)
    dat.append(total)
    return dat

def stop(update, context):
    userdata = context.dispatcher.user_data
    for x,y in userdata.items():
        chatID=str(x)
    with open('ids.txt','r') as f:
        data=f.read()
    data=data.split('\n')
    if chatID in data:
        data.remove(chatID)
        with open('ids.txt','w') as f:
            for ids in data:
                f.write(str(ids)+"\n")
            print('Reemoved a user.Final Count:'+str(len(list(dict.fromkeys(data)))))
    update.message.reply_text("Sorry to see you go.\nIf you could please drop a quick feedback at https://forms.gle/aRuUcrmg6trZX1wt7\n\nStay safe.",
        reply_markup=markup)
    return CHOOSING

def start(update, context):
    userdata = context.dispatcher.user_data
    for x,y in userdata.items():
        chatID=str(x)
    with open('ids.txt','r') as f:
        data=f.read()
    data=data.split('\n')
    if chatID not in data:
        data.append(chatID)
        with open('ids.txt','w') as f:
            for ids in data:
                f.write(str(ids)+"\n")
            messageWithPurpose("Hey! Welcome to COVID-19 India Bot.\nWhat can this bot do?\n\nCOVID-19 India is a telegram bot to keep people updated about count of people affected by COVID19 India. \n\nWe also aim to provide you verified developments/news regarding this so as to prevent circulation of fake news and the tensions cause by it. \n\nSource for number : covid19india.org\n\n Send a /stop message to stop receiving further updates.\n\nPlease share with your Famiy and Friends",chatID)
            update.message.reply_text("COVID-19 India bot : Live and verified information about COVID cases in India.\nLink: http://t.me/COVID19IND1A_BOT")
            print('Count:'+str(len(list(dict.fromkeys(data)))))
    count=get_stats_total()
    update.message.reply_text("Total number of COVID-19 Cases in India : "+str(count)+"\nSelect a state to get statewise summary.",
        reply_markup=markup)
    return CHOOSING

def regular_choice(update, context):
    text = update.message.text
    if text=="India":
        count=get_stats_total()
        mData=mAllInfo()
        msg="Number of all COVID-19 cases in " + text +" : " + str(count)+"\n\nNumber of Cured cases : "+str(mData[1])+"\n\nNumber of Deaths : "+str(mData[2])
        update.message.reply_text(msg,reply_markup=markup)
        return CHOOSING
    count=get_state_total(text)
    mData=mStateInfo(text)
    if len(mData)!=0:
        msg="Number of all COVID-19 cases in " + text +" : " + str(count[1])+"\n\nNumber of Cured cases : "+str(mData[1])+"\n\nNumber of Deaths : "+str(mData[2])
    else:
        msg="Number of all COVID-19 cases in " + text +" : " + str(count[1])
    update.message.reply_text(msg+"\n\nDistrictwise distribution - \n\n"+count[0],reply_markup=markup)
    return CHOOSING


def custom_choice(update, context):
    update.message.reply_text("Wooops!I don't understand this.Just programmed to do one thing -\nTo get number of people affected by COVID-19.\nPick a state for details.",reply_markup=markup)
    return CHOOSING

def done(update, context):
    return ConversationHandler.END

def help(update, context):
    update.message.reply_text("COVID-19 India is a telegram bot to keep people updated about count of people affected by COVID-19 India.\n\nWe also aim to provide you verified developments/news regarding this so as to prevent circulation of fake news and the tensions caused by it.\n\nData-Source : covid19india.org and api.rootnet.in\n\nSend a /start message to proceed.",reply_markup=markup)
    return CHOOSING


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(BOTTOKEN, use_context=True, request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(Filters.regex('^(India|Delhi|Andhra Pradesh|Arunachal Pradesh|Assam|Bihar|Chhattisgarh|Goa|Gujarat|Haryana|Himachal Pradesh|Jharkhand|Karnataka|Kerala|Madhya Pradesh|Maharashtra|Manipur|Mizoram|Odisha|Punjab|Rajasthan|Tamil Nadu|Telangana|Uttar Pradesh|Uttarakhand|West Bengal|Ladakh|Jammu and Kashmir|Puducherry|Chandigarh|Andaman and Nicobar Islands)$'),
                                      regular_choice),
                      MessageHandler(Filters.regex('^Done$'), done),
                      MessageHandler(Filters.text, custom_choice)
                       ],
                },

        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)]
    )
    dp.add_handler(MessageHandler(Filters.regex('^(India|Delhi|Andhra Pradesh|Arunachal Pradesh|Assam|Bihar|Chhattisgarh|Goa|Gujarat|Haryana|Himachal Pradesh|Jharkhand|Karnataka|Kerala|Madhya Pradesh|Maharashtra|Manipur|Mizoram|Odisha|Punjab|Rajasthan|Tamil Nadu|Telangana|Uttar Pradesh|Uttarakhand|West Bengal|Ladakh|Jammu and Kashmir|Puducherry|Chandigarh|Andaman and Nicobar Islands)$'),regular_choice))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
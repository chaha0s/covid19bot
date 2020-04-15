import requests
import json
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import urllib.parse

from getInformation import *
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING = range(1)

reply_keyboard = [["India"],["Delhi","Andhra Pradesh"],["Arunachal Pradesh","Assam"],["Bihar","Chhattisgarh"],["Goa","Gujarat"],["Haryana","Himachal Pradesh"],["Jharkhand","Karnataka"],["Kerala","Madhya Pradesh"],["Maharashtra","Manipur"],["Mizoram","Odisha"],["Punjab","Rajasthan"],["Tamil Nadu","Telangana"],["Uttar Pradesh","Uttarakhand"],["West Bengal","Ladakh"],["Jammu and Kashmir","Puducherry"],["Chandigarh","Andaman and Nicobar Islands"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def start(update, context):
    msg="Comparision of COVID-19 data between MOHFW and COVID19INDIA\nSelect a state : "
    update.message.reply_text(msg,reply_markup=markup)
    return CHOOSING

def regular_choice(update, context):
    text = update.message.text
    if text=="India":
        count=get_stats_total()
        mData=mAllInfo()
        msg="MOHFW : "+ str(count)+"\n\n"+"COVID19INDIA : "+str(mData)
        update.message.reply_text(msg,reply_markup=markup)
        return CHOOSING
    count=get_state_total(text)
    mData=mStateInfo(text)
    msg="MOHFW : "+ str(count)+"\n\n"+"COVID19INDIA : "+str(mData)
    update.message.reply_text(msg,reply_markup=markup)
    # update.message.reply_text(msg,reply_markup=markup)
    return CHOOSING


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("971181131:AAGBI7d0OpJQOOpy0FKDixuTJZnXP_HunqA", use_context=True, request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^(India|Delhi|Andhra Pradesh|Arunachal Pradesh|Assam|Bihar|Chhattisgarh|Goa|Gujarat|Haryana|Himachal Pradesh|Jharkhand|Karnataka|Kerala|Madhya Pradesh|Maharashtra|Manipur|Mizoram|Odisha|Punjab|Rajasthan|Tamil Nadu|Telangana|Uttar Pradesh|Uttarakhand|West Bengal|Ladakh|Jammu and Kashmir|Puducherry|Chandigarh|Andaman and Nicobar Islands)$'),regular_choice))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
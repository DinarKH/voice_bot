from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re
import html
from TTS import TTS
import os
from configs import settings

mercury_api_key=settings['mercury_api_key']
yandex_api_key=settings['yandex_api_key']
updater=Updater(settings['telegram_api_key'])

def start(bot, update):
    update.message.reply_text(settings['start_mess'])

def help(bot, update):
    update.message.reply_text(settings['help_mess'])

def check(bot, update):
    update.message.reply_text("Началась обработка запроса")
    input=update.message.text
    c_i = update.message.chat_id
    my_text=""
    my_text = myParse(input,update)
    len_t=len(my_text)
    if (len_t>0):
        update.message.reply_text("Длина текста {} среднее время ожидания {} минут {} секунд".format\
                                      (len_t,len_t//6000,len_t%60))
        to_audio(my_text,update)
        update.message.reply_text("Файл готов")
        bot.send_audio(chat_id=c_i, audio=open("Speech/{}.mp3".format(c_i), "rb"))
        os.remove("Speech/{}.mp3".format(c_i))

def myParse(site_name,update):
    r=requests.get("https://mercury.postlight.com/parser?url="
                   +site_name,headers={"Content-Type": "application/json",
                   "Accept-Language": "ru-RU","x-api-key":mercury_api_key})
    dic=r.json()
    tag_re = re.compile(r'<[^>]+>')
    parsed_text=""
    try:
        no_tags = tag_re.sub('', dic['content'])
        parsed_text=html.unescape(no_tags)
    except Exception:
        update.message.reply_text(settings['err_mess'])
    return parsed_text

def to_audio(my_text,update):
    view_size = 0
    step = 1500 #max text to speech 1500 symbols
    num = 1
    while view_size<len(my_text):
        my_string=my_text[view_size:view_size+step]
        make_speech(my_string,num,update)
        view_size+=step
        num+=1

def make_speech(text,num,update):
    tts = TTS(yandex_api_key,speaker="oksana")
    tts.generate(text)
    tts.save("Speech/{}.mp3".format(update.message.chat_id))
    #спамит чат, но показывет, пользователю, что бот работает
    # if(n%6==0):
    #     update.message.reply_text("Уже обработано {} символов".format(num*1500))

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.text, callback=check))

updater.start_polling()
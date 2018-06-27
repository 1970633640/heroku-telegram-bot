# -*- coding: utf-8 -*-
from telebot import TeleBot
import requests
import os

# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
# some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis


#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
app = TeleBot(__name__)


def mid(s, l, r):
    l1 = s.find(l) + len(l)
    r1 = s[l1:].find(r) + l1
    return s[l1:r1]


@app.route('/advanced ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = user_msg
    # --
    try:
        cnt=int(msg.split()[1])
        key=' '.join(msg.split()[2:])
        app.send_message(chat_dest, "%s %s"%(cnt,key))
        r = requests.get("http://f.cili001.com/index/index?c=&k=" + key)
        for i in range(1, cnt):
            first = r.text.split("<ul class=\"link-list\">")[i]
            # print(first)
            mag = mid(first, 'data-magnet="', '"')
            name = mid(first, '<span class="name">', '</span>').replace('[CiLi001.com]','')
            size = mid(first, '<span class="size">', '</span>')
            time = mid(first, '<span class="time">', '</span>')
            date = mid(first, '<p class="link-list-title">', '</p>').strip()
            msg2 = "结果%s:\n%s\n%s %s\n大小: %s\n磁力链接:" % (i,name,date, time, size)
            msg3=mag
            # --
            app.send_message(chat_dest, msg2)
            app.send_message(chat_dest, msg3)
    except:
        app.send_message(chat_dest, "搜索失败")


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = user_msg
    # --
    try:
        r = requests.get("http://f.cili001.com/index/index?c=&k=" + msg)
        first = r.text.split("<ul class=\"link-list\">")[1]
        # print(first)
        mag = mid(first, 'data-magnet="', '"')
        name = mid(first, '<span class="name">', '</span>').replace('[CiLi001.com]','')
        size = mid(first, '<span class="size">', '</span>')
        time = mid(first, '<span class="time">', '</span>')
        date = mid(first, '<p class="link-list-title">', '</p>').strip()
        msg2 = "%s\n%s %s\n大小: %s\n磁力链接:" % (name,date, time, size)
        msg3=mag
        # --
        app.send_message(chat_dest, msg2)
        app.send_message(chat_dest, msg3)
    except:
        app.send_message(chat_dest, "搜索失败")




if __name__ == '__main__':
    app.config['api_key'] = token
    app.poll(debug=True)

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


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "命令1: {}".format(cmd)
    app.send_message(chat_dest, msg)



@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = user_msg
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = token
    app.poll(debug=True)
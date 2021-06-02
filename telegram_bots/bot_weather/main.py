from datetime import datetime
import os
import json
import errno
import subprocess
import logging
from logging.handlers import TimedRotatingFileHandler

from decouple import config
import telebot

from matrix.conversation import MessageConversation, CallConversation
from clients.info import GetUserInfo
from telegram_bots.bot_weather.api_req.api_requests import ApiRequests


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_ENV_DIR = config('LOGS_ENV_DIR_NAME')
ABSOLUTE_LOGS_DIR = None


TELEGRAM_TOKEN = config('TBOT_WEATHERME_TOKEN')
MESSAGES_TO_DEL = set()
USER_INFO = dict()
USER_CAR_INFO_DICT = dict()

bot = telebot.TeleBot(TELEGRAM_TOKEN)
bot_user = bot.get_me()

BOT_NAME = bot_user.first_name
BOT_ID = bot_user.id
BOT_USERNAME = bot_user.username


# ┌========================================== LOGGING ==================================================┐
try:
    container_id = subprocess.check_output('cut -c9-20 < /proc/1/cpuset', shell=True, universal_newlines=True)[:-1]
except subprocess.SubprocessError as e:
    container_id = 'NotDocker'
    print(e)
    print(f"You are using not docker container build! 'container_id' in logs will be set as '{container_id}'")


if container_id != 'NotDocker':
    ABSOLUTE_LOGS_DIR = os.path.join(LOGS_ENV_DIR)
    if not os.path.exists(ABSOLUTE_LOGS_DIR):
        os.makedirs(ABSOLUTE_LOGS_DIR)
else:
    ABSOLUTE_LOGS_DIR = os.path.join(PROJECT_DIR, LOGS_ENV_DIR)
    if not os.path.exists(ABSOLUTE_LOGS_DIR):
        os.makedirs(ABSOLUTE_LOGS_DIR)

LOGS_FILE = os.path.join(ABSOLUTE_LOGS_DIR, f"{BOT_USERNAME}.log")
print('LOGS_FILE: ', LOGS_FILE)
print('PROJECT_DIR: ', PROJECT_DIR)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : [' + container_id + '] :[%(filename)s.%(lineno)d]: %(levelname)s : %(message)s',
    handlers=[TimedRotatingFileHandler(LOGS_FILE, when="midnight")])

logger = logging.getLogger(__name__)
logger.info(f'\n\n=!= Start TBot =!=\nbot_id:       {BOT_ID}\nbot_name:     {BOT_NAME}\nbot_username: {BOT_USERNAME}\n'
            f'logs:         {LOGS_FILE}'
            f'project_dir:  {PROJECT_DIR}')
logger.info(f'')


class LogMe:
    @staticmethod
    def log(message, answer):
        log_string = f"""
        --------
        {datetime.now()}
        From: {message.from_user.username} ({message.from_user.first_name} {message.from_user.last_name}). 
        ID: {str(message.from_user.id)}
        Text: {message.text}
        Answer: {answer}
        Location: {message.location}
        """
        return log_string

# └========================================== LOGGING ==================================================┘


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "menu":
        CallConversation(t_bot=bot, t_call=call).main_menu()
    elif call.data == "update_town_list":
        CallConversation(t_bot=bot, t_call=call).delete_two_call()
        CallConversation(t_bot=bot, t_call=call).call_api_update()
        bot.register_next_step_handler(call.message, api_update_town_list)
    elif call.data == "chose_one_town":
        CallConversation(t_bot=bot, t_call=call).delete_two_call()
        CallConversation(t_bot=bot, t_call=call).call_api_chose_one()
        bot.register_next_step_handler(call.message, api_chose_one_town)
    elif call.data == "chose_many_towns":
        CallConversation(t_bot=bot, t_call=call).delete_two_call()
        CallConversation(t_bot=bot, t_call=call).call_api_chose_many()
        bot.register_next_step_handler(call.message, api_chose_many_towns)
    # elif call.data == "show_ten":
    #     CallConversation(t_bot=bot, t_call=call).delete_two_call()
    #     CallConversation(t_bot=bot, t_call=call).call_api_show_ten()
    #     bot.register_next_step_handler(call.message, api_show_ten)


@bot.message_handler(commands=['help'])
def handle_help(message):
    MessageConversation(t_bot=bot, t_message=message).answer_help_info()


@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Weather bot at your service!
    """
    MessageConversation(t_bot=bot, t_message=message).answer_welcome()
    logger.info(GetUserInfo(t_message=message).gather_fields())
    MessageConversation(t_bot=bot, t_message=message).main_menu()


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if "погода" in message.text:
        MessageConversation(t_bot=bot, t_message=message).answer_weather()
        logger.info(LogMe.log(message, 'answer_weather'))
    elif "API" in message.text:
        MessageConversation(t_bot=bot, t_message=message).delete_one_message()
        MessageConversation(t_bot=bot, t_message=message).answer_api()
        logger.info(LogMe.log(message, 'answer_api'))


@bot.message_handler(content_types=['location'])
def handle_location(message):
    if message.location is not None:
        # latitude - широта, longitude - долгота
        MessageConversation(t_bot=bot, t_message=message).answer_your_location()
        logger.info(LogMe.log(message, 'user_location'))


def api_update_town_list(message):
    try:
        msg = message.text
        if msg == "send-default-towns":
            rq = ApiRequests.send_town_list()
        else:
            rq = ApiRequests.send_town_list(*[str(i) for i in msg.split()])
        # bot.register_next_step_handler(msg, car_dialog_name)
        text = 'Updated:\n'
        for k, v in json.loads(rq.text).items():
            text += f'{v} - {k}\n'
        MessageConversation(t_bot=bot, t_message=message).send_msg(text)
    except Exception as err:
        logger.error(err)
        MessageConversation(t_bot=bot, t_message=message).send_msg(err)


def api_chose_one_town(message):
    # TODO:
    #  1. Request for town_list = """1 Moscow"""
    try:
        msg = message.text
        if msg == "send-default-number":
            rq = ApiRequests.get_one_town(1)
        else:
            rq = ApiRequests.get_one_town(int(msg))
        text = 'Town:\n'
        for k, v in json.loads(rq.text).items():
            text += f'{k}: {v}\n'
        MessageConversation(t_bot=bot, t_message=message).send_msg(text)
    except Exception as err:
        logger.error(err)
        MessageConversation(t_bot=bot, t_message=message).send_msg(err)


def api_chose_many_towns(message):
    try:
        msg = message.text
        if msg == "send-default-range":
            rq = ApiRequests.get_many_towns(1, 2)
        else:
            msg = [int(i) for i in msg.split()]
            rq = ApiRequests.get_many_towns(msg[0], msg[1])
        text = 'Towns info:\n'
        for k, v in json.loads(rq.text).items():
            text += f'{k}: {v}\n'
        text_bytes = bytearray(text.encode())
        MessageConversation(t_bot=bot, t_message=message).send_fl(text_bytes)
    except Exception as err:
        logger.error(err)
        MessageConversation(t_bot=bot, t_message=message).send_msg(err)


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will happen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

# start TBot
bot.polling(none_stop=True)

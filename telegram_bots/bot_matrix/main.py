import time
from datetime import datetime
import os
import errno
import subprocess
import logging
from logging.handlers import TimedRotatingFileHandler

from decouple import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from matrix.conversation import MatrixConversation
from clients.info import GetUserInfo, CarUser
from matrix.markups import user_keyboard_markup
from matrix.stickers import StickerRelpy


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_ENV_DIR = config('LOGS_ENV_DIR_NAME')
ABSOLUTE_LOGS_DIR = None


TELEGRAM_TOKEN = config('TBOT_THE_MATRIX_TOKEN')
MESSAGES_TO_DEL = set()
USER_INFO_LIST = {}
USER_CAR_INFO_DICT = dict()

bot = telebot.TeleBot(TELEGRAM_TOKEN)
bot_user = bot.get_me()

BOT_NAME = bot_user.first_name
BOT_ID = bot_user.id
BOT_USERNAME = bot_user.username
# bot_user.wait()


STICKER_RED_WOMAN = 'AgADbgIAAtzyqwc'
STICKER_NEO = 'AgADeQIAAtzyqwc'
STICKER_NEO_EVASION = 'AgADaQIAAtzyqwc'
STICKER_MORPHEUS = 'AgADeAIAAtzyqwc'
STICKER_RABBIT = 'AgADbAIAAtzyqwc'
STICKER_TRINITY_HI = 'AgADNwQAAj-VzAo'
STICKER_TRINITY_SHH = 'AgADOAQAAj-VzAo'
STICKER_TRINITY_ADVICE = 'AgADPgQAAj-VzAo'
STICKER_TRINITY_LOVE = 'AgADdQIAAtzyqwc'

with open('tbot_data/stop_words/stopwords.txt') as f:
    WORD_SET_STOPWORDS_RU = set(f.readline().split())
WORD_SET_WELCOME_GREETING = {
    'ghbdtn', 'привет', 'салют', 'прт', 'q', 'qq', 'hi', 'hello', 'hola', 'добрый вечер', 'добрый'}


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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : [' + container_id + '] :[%(filename)s.%(lineno)d]: %(levelname)s : %(message)s',
    handlers=[TimedRotatingFileHandler(LOGS_FILE, when="midnight")])

logger = logging.getLogger(__name__)
logger.info(f'\n\n=!= Start TBot =!=\nbot_id:       {BOT_ID}\nbot_name:     {BOT_NAME}\nbot_username: {BOT_USERNAME}\n')
logger.info(f'')
# └========================================== LOGGING ==================================================┘

# @bot.message_handler(content_types=[
#     'audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])


def log(message, answer):
    print("\n --------")
    print(datetime.now())
    print("Сообщение от {0} ({1} {2}). (id: {3})\n Текст: {4}".format(
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name,
        str(message.from_user.id),
        message.text))
    print(" Ответ:", answer)
    print(" Местоположение:", message.location)


def slow_typing(message, text, speed=0.2):
    string = ''
    for letter in text:
        if letter == ' ':
            string += letter
            continue
        else:
            string += letter
            bot.edit_message_text(text=string,
                                  chat_id=message.chat.id,
                                  message_id=message.message_id + 1,
                                  parse_mode='markdown')
            # inline_message_id='2')
            time.sleep(speed)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "rabbit_yes":
        MatrixConversation(tbot=bot, tcall=call).rabbit_question()
        USER_INFO_LIST = GetUserInfo(tmessage=call).gather_fields()
        print(USER_INFO_LIST)
    elif call.data == "trinity_yes1":
        MatrixConversation(tbot=bot, tcall=call).trinity_question_in_club()
    elif call.data == "trinity_yes2":
        MatrixConversation(tbot=bot, tcall=call).trinity_question_in_hostel()
    elif call.data == "trinity_yes3":
        MatrixConversation(tbot=bot, tcall=call).morpheus_question_in_hostel()
    elif call.data == "morpheus_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
        MatrixConversation(tbot=bot, tcall=call).end_questions_yes()
    elif call.data == "morpheus_no":
        bot.answer_callback_query(call.id, "Answer is No")
        MatrixConversation(tbot=bot, tcall=call).delete_two_call()
        MatrixConversation(tbot=bot, tcall=call).show_reality()
    elif call.data == "woman_in_red_yes":
        MatrixConversation(tbot=bot, tcall=call).extra_woman_in_red()
    elif call.data == "alarm_yes":
        MatrixConversation(tbot=bot, tcall=call).rabbit_question()
        USER_INFO_LIST = GetUserInfo(tmessage=call).gather_fields()
        print(USER_INFO_LIST)
    elif call.data == "alarm_no":
        MatrixConversation(tbot=bot, tcall=call).delete_one_call()


@bot.message_handler(commands=['help'])
def handle_help(message):
    MatrixConversation(tbot=bot, tmessage=message).answer_help_info()


@bot.message_handler(commands=['start'])
def handle_start(message):
    """
    Wake up, Neo...
    The Matrix has you...
    Follow the white rabbit...
    You are not the one. Wake up!
    """
    bot.send_message(message.chat.id, text='_')
    time.sleep(0.5)
    text = r'Wake up, Neo...'
    slow_typing(message=message, text=text, speed=0.1)
    text = r'The Matrix has you...'
    slow_typing(message=message, text=text, speed=0.1)
    text = r'Follow the white rabbit...'
    slow_typing(message=message, text=text, speed=0.2)
    text = r'Knock, knock, Neo.'
    slow_typing(message=message, text=text, speed=0)
    MatrixConversation(tbot=bot, tmessage=message).start_questions()


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(chat_id=message.from_user.id,
                     text="""
    *Агент Смит:*
    Счастье в неведении.
    """, reply_markup=hide_markup, parse_mode='markdown')
    bot.send_chat_action(message.chat.id, 'typing')


@bot.message_handler(commands=['show_my_photo'])
def handle_help(message):
    MatrixConversation(tbot=bot, tmessage=message).answer_show_uploaded_photo()


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    print("message: ", message)
    print("file_id: ", message.sticker.file_id)
    print("file_unique_id: ", message.sticker.file_unique_id)
    print("emoji: ", message.sticker.emoji)
    print("from: ", message.json.get('from'))
    StickerRelpy(tbot=bot, tmessage=message).compare_sticker_with(sticker=STICKER_NEO)
    StickerRelpy(tbot=bot, tmessage=message).compare_sticker_with(sticker=STICKER_TRINITY_LOVE)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    USER_INFO_LIST = GetUserInfo(tmessage=message).gather_fields()
    print(USER_INFO_LIST)

    # TODO: put in dict/list WELCOME_PHRASES = []
    #   parsed_text = check_message(message.text)
    if "привет" in message.text or "ghbdtn" in message.text or "hi" in message.text or "hello" in message.text:
        MatrixConversation(tbot=bot, tmessage=message).answer_hello()
        log(message, 'answer_hello')
        MatrixConversation(tbot=bot, tmessage=message).answer_empty_with_markup(user_keyboard_markup())
    elif message.text == "фото":
        MatrixConversation(tbot=bot, tmessage=message).answer_photo()
        log(message, 'answer_file')
    elif message.text == "... ->":
        MatrixConversation(tbot=bot, tmessage=message).extra_menu()
    elif message.text == "назад":
        MatrixConversation(tbot=bot, tmessage=message).delete_one_message()
        MatrixConversation(tbot=bot, tmessage=message).main_menu()
    elif message.text == "кто я?":
        MatrixConversation(tbot=bot, tmessage=message).answer_whoami(user_info_dict=USER_INFO_LIST)
        log(message, 'answer_whoami')
    elif message.text == "где мы?":
        MatrixConversation(tbot=bot, tmessage=message).answer_my_position()
        log(message, 'answer_whoami')
    elif message.text == "погода":
        MatrixConversation(tbot=bot, tmessage=message).answer_weather()
        log(message, 'answer_weather')
    elif message.text == '💕️':  # ❤
        MatrixConversation(tbot=bot, tmessage=message).answer_heart()
        log(message, 'answer_heart')
    elif message.text == '🚘':
        # FIXME:
        #   register_next_step_handler -> don't work with classes ->
        #   TypeError: cannot pickle '_thread.lock' object
        #   MatrixConversation(tbot=bot, tmessage=message).answer_start_car_conversation()
        #   https://stackoverflow.com/questions/44144584/typeerror-cant-pickle-thread-lock-objects
        #   https://stackoverflow.com/questions/7865430/multiprocessing-pool-picklingerror-cant-pickle-type-thread-lock-attribu
        car_start_conversation(message)
        log(message, 'answer_start_car_conversation')
    elif message.text == "show me keyboard markup":
        MatrixConversation(tbot=bot, tmessage=message).stackoverflow()
    else:
        dont_stop_words_flag = True
        try:
            for word in message.text.split():
                if word.lower() in WORD_SET_STOPWORDS_RU:
                    dont_stop_words_flag = False
            if not dont_stop_words_flag:
                MatrixConversation(tbot=bot, tmessage=message).answer_angry()
        except:
            pass
        if dont_stop_words_flag:
            MatrixConversation(tbot=bot, tmessage=message).answer_morpheus_welcome(
                bot_name=BOT_NAME,
                bot_username=BOT_USERNAME)
            log(message, 'answer_morpheus_welcome')
        # MatrixConversation(tbot=bot, tmessage=message).answer_empty_with_markup(user_keyboard_markup())


@bot.message_handler(content_types=['location'])
def handle_lcation(message):
    if message.location is not None:
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        # bot.send_chat_action(chat_id=message.from_user.id, action='find_location')
        # latitude - широта, longitude - долгота
        MatrixConversation(tbot=bot, tmessage=message).answer_your_location()
        log(message, 'user_location')


@bot.message_handler(content_types=['video'])
def handle_video(message):
    print("message: ", message)
    print("file_id: ", message.sticker.file_id)
    print("file_unique_id: ", message.sticker.file_unique_id)
    print("from: ", message.json.get('from'))


def processPhotoMessage(message):
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)

    USER_INFO_LIST = GetUserInfo(tmessage=message).gather_fields()
    print(USER_INFO_LIST)

    folder = 'clients_data'
    owner = USER_INFO_LIST.get("id")
    name = file.file_path.split('/')[-1]
    # name = USER_INFO_LIST.get("id") + '.jpg'
    filepath = os.path.join(folder, owner, name)

    print('message.photo =', message.photo)
    print('fileID =', fileID)
    print('file.file_path =', file.file_path)
    print('filename =', filepath)

    downloaded_file = bot.download_file(file.file_path)
    if not os.path.exists(os.path.dirname(filepath)):
        try:
            os.makedirs(os.path.dirname(filepath))
        except OSError as exc:  # Guard against race condition
            print(exc)
            if exc.errno != errno.EEXIST:
                raise
    try:
        with open(filepath, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as e:
        print(e)


@bot.message_handler(content_types=['photo'])
def photo(message):
    processPhotoMessage(message)


def car_start_conversation(message):
    msg = bot.reply_to(message=message,
                       text="""\
    *Тринити:*
    Хорошо, Нео.
    Приступим к регистрации твоих данных
    в системе (Расскажи о Себе и о Тачке)! 
    Отвечай честно, это лишь формальность.

*Твое полное имя?:*
    """, parse_mode='markdown')
    bot.register_next_step_handler(msg, car_dialog_name)


def car_dialog_name(message):
    try:
        chat_id = message.chat.id
        name = message.text
        if len(name) > 25:
            name = "WRONG"
        new_user = CarUser(user_id=message.from_user.id, user_nickname=message.from_user.username, name=name)
        USER_CAR_INFO_DICT[chat_id] = new_user

        msg = bot.reply_to(message=message, text="""*Твоя фамилия?:*""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_surname)
    except Exception as err:
        logger.error(err)
        bot.reply_to(message, 'oooops')


def car_dialog_surname(message):
    try:
        chat_id = message.chat.id
        surname = message.text
        if len(surname) > 25:
            surname = "WRONG"

        the_user = USER_CAR_INFO_DICT[chat_id]
        the_user.surname = surname

        markup = ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Anderson', 'Smith')

        msg = bot.reply_to(message=message,
                           text="""*Отчество?:* \n(не важно, можешь выбрать из меню на клавиатуре)""",
                           parse_mode='markdown',
                           reply_markup=markup)

        bot.register_next_step_handler(msg, car_dialog_last_name)
    except Exception as err:
        logger.error(err)
        bot.reply_to(message, 'oooops')


def car_dialog_last_name(message):
    try:
        chat_id = message.chat.id
        user_last_name = message.text
        if len(user_last_name) > 25:
            user_last_name = "WRONG"

        the_user = USER_CAR_INFO_DICT[chat_id]
        if (user_last_name == u'Anderson') or (user_last_name == u'Smith'):
            the_user.lastname = user_last_name

        the_user.lastname = user_last_name

        markup = ReplyKeyboardMarkup(one_time_keyboard=True)
        msg = bot.reply_to(message=message, text="""*Сколько лет?:*""", parse_mode='markdown', reply_markup=None)
        bot.register_next_step_handler(msg, car_dialog_age)
    except Exception as err:
        logger.error(err)
        bot.reply_to(message, 'oooops')


def car_dialog_age(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, """Возраст должен быть числом.\n*Сколько лет?:*""", parse_mode='markdown')
            bot.register_next_step_handler(msg, car_dialog_age)
            return
        the_user = USER_CAR_INFO_DICT[chat_id]
        the_user.age = age

        markup = ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message=message, text="""*Пол?:*""", parse_mode='markdown', reply_markup=markup)
        bot.register_next_step_handler(msg, car_dialog_sex)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_sex(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            the_user.sex = sex
        else:
            raise Exception("Unknown sex")

        now = datetime.now()
        if the_user.sex == u'Male':
            sex_print = 'Мужчина'
        else:
            sex_print = 'Женжина'

        bot.send_message(chat_id=chat_id,
                         text=f"""
    *Агент Смит:* 
    (Кладет перед вами папку)

```
ДЕЛО № {the_user.user_id}
ОТ: {now.strftime("%d/%m/%Y %H:%M")}

{the_user.name}
{the_user.surname}
{the_user.lastname}
{the_user.age} года 
{sex_print}
```

        """, parse_mode='markdown')

        markup = ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Yes', 'No')

        bot.send_message(chat_id=chat_id,
                         text=f"""
    *Агент Смит:*
    Приготовь:

```
- СВИДЕТЕЛЬСВО О РЕГИИСТРАЦИИ ТС
- ВОДИТЕЛЬСКОЕ УДОСТОВЕРЕНИЕ
```
                """, parse_mode='markdown')

        msg = bot.reply_to(message=message, text="""*Готов продолжить?:*""", parse_mode='markdown', reply_markup=markup)
        bot.register_next_step_handler(msg, car_dialog_yes_no)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_yes_no(message):
    try:
        chat_id = message.chat.id
        yes_no = message.text

        if yes_no.lower() == 'yes':
            msg = bot.reply_to(message=message, text="""*Город регистрации ТС?:*""", parse_mode='markdown')
            bot.register_next_step_handler(msg, car_dialog_city)
        else:
            return
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_city(message):
    try:
        chat_id = message.chat.id
        city = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.city = city
        msg = bot.reply_to(message=message, text="""*Номер свидетельства о регистрации ТС?:*
(формат: ```7788№777111```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_certificate_of_registration_number)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_certificate_of_registration_number(message):
    try:
        chat_id = message.chat.id
        certificate_number = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_certificate_of_registration_number = certificate_number
        msg = bot.reply_to(message=message, text="""*Номер ТС?:*
(формат: ```К555АО177```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_number)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_number(message):
    try:
        chat_id = message.chat.id
        car_number = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_number = car_number
        msg = bot.reply_to(message=message, text="""*VIN номер ТС?:*
(формат: ```JN1CCCA33U2266333```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_vin)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_vin(message):
    try:
        chat_id = message.chat.id
        car_vin = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_vin = car_vin
        msg = bot.reply_to(message=message, text="""*Марка, модель ТС?:*
(формат: ``` NISSAN MATRIX ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_model)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_model(message):
    try:
        chat_id = message.chat.id
        car_model = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_model = car_model
        msg = bot.reply_to(message=message, text="""*Тип ТС?:*
(формат: ``` Легковой седан ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_type)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_type(message):
    try:
        chat_id = message.chat.id
        car_type = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_type = car_type
        msg = bot.reply_to(message=message, text="""*Год выпуска ТС?:*
(формат: ``` 2005 ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_manufacture_year)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_manufacture_year(message):
    try:
        chat_id = message.chat.id
        car_manufacture_year = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_manufacture_year = car_manufacture_year
        msg = bot.reply_to(message=message, text="""*Цвет ТС?:*
(формат: ``` Серый ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_color)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_color(message):
    try:
        chat_id = message.chat.id
        car_color = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_color = car_color
        msg = bot.reply_to(message=message, text="""*Мощность двигателя, кВТ/л.с ТС?:*
(формат: ``` 120.0/150 ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_engine_power)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_engine_power(message):
    try:
        chat_id = message.chat.id
        car_engine_power = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_engine_power = car_engine_power
        msg = bot.reply_to(message=message, text="""*Паспорт ТС?:*
(формат: ``` 55СА№07788 ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_car_passport_number)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_car_passport_number(message):
    try:
        chat_id = message.chat.id
        car_passport_number = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        the_user.car_passport_number = car_passport_number
        msg = bot.reply_to(message=message, text="""*xxxxx ТС?:*
(формат: ``` xxxxx ```)""", parse_mode='markdown')
        bot.register_next_step_handler(msg, car_dialog_print_cert)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_print_cert(message):
    try:
        chat_id = message.chat.id
        print_msg = message.text
        the_user = USER_CAR_INFO_DICT[chat_id]

        now = datetime.now()

        bot.send_message(chat_id=chat_id,
                         text=f"""
        *Агент Смит:* 
        (Медленно раскручивает шнурок на толстой папке и открывает)

```
ДЕЛО № {the_user.user_id}
ОТ: {now.strftime("%d/%m/%Y %H:%M")}

{the_user.name}
{the_user.surname}
{the_user.lastname}
{the_user.age} года 
{the_user.sex}
```

```
СВИДЕТЕЛЬСВО О РЕГИИСТРАЦИИ ТС:
Город: {the_user.city}
Номер свидетельства: {the_user.car_certificate_of_registration_number}
Номер машины: {the_user.car_number}
VIN: {the_user.car_vin}
Модель: {the_user.car_model}
Тип: {the_user.car_type}
Год выпуска: {the_user.car_manufacture_year}
Цвет: {the_user.car_color}
Мощность двигателя: {the_user.car_engine_power}
Паспорт ТС: {the_user.car_passport_number}
Масса разрешенная max: {the_user.car_weight_max}
Масса без нагрузки min: {the_user.car_weight_min}
```
            """, parse_mode='markdown')

        markup = ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Yes', 'No')

        bot.send_message(chat_id=chat_id,
                         text=f"""
*Агент Смит:* 
Как вы видите, мы за Вами давненько наблюдаем, мистер {the_user.lastname}. 
Оказывается Вы живете двойной жизнью. 
В одной жизни Вы - {the_user.name} {the_user.surname[:1]}. {the_user.lastname}, 
программист в крупной уважаемой компании. 
У Вас есть медицинская страховка, Вы платите налоги и еще - 
помогаете консьержке выносить мусор.
Другая Ваша жизнь - в компьютерах. 
И тут Вы известны как хакер {the_user.user_nick}. Вы виновны практически во 
всех уголовно наказуемых компьютерных преступлениях. 
У первого - {the_user.name} - есть будущее. 
У {the_user.user_nick} - нет.
Буду предельно откровенен с Вами, мистер {the_user.surname}. 

*Теперь Вам доступны новые возможности в Меню:*
```
- проверка штрафов
- запрос на поиск деталей по VIN
- ну и другие плюшки
```
                    """, parse_mode='markdown')

        msg = bot.reply_to(message=message, text="""*Готов продолжить?:*""", parse_mode='markdown', reply_markup=markup)
        bot.register_next_step_handler(msg, car_dialog_all_correct)
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


def car_dialog_all_correct(message):
    try:
        chat_id = message.chat.id
        yes_no = message.text

        if yes_no.lower() == 'yes':
            msg = bot.reply_to(message=message, text="""*Yes:*""", parse_mode='markdown')
            return
        else:
            msg = bot.reply_to(message=message, text="""*No:*""", parse_mode='markdown')
            return
    except Exception as e:
        logger.error(e)
        bot.reply_to(message, 'oooops')


#
# @bot.callback_query_handler(func=lambda call: True)
# def test_callback(call):
#     print("Call:", call)
#
# @bot.message_handler(func=check_answer)
# def handle_message(message):
#     print(message)
#     bot.send_message(
#         chat_id=message.chat.id,
#         text='What are you talking about?\nDo you want to see the Truth or Not?')
#     # Morpheus
#     bot.send_sticker(
#         chat_id=message.chat.id,
#         data='CAACAgIAAxkBAANbYINHPGkKa6MZBeuygEKzQJzzp1sAAngCAALc8qsHISNlidiEbn4fBA')
#
# @bot.message_handler(content_types=[
#     'audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
# def handle_message(message):
#     message.chat.type = 'private'
#     print("Text IN: ", message.text)
#     print("Json IN: ", message)
#     # print(kwargs)
#
#     bot.send_message(
#         chat_id=message.chat.id,
#         text='Wake up,')
#     time.sleep(0.5)
#     bot.edit_message_text(text='Wake up, Neo!',
#                           chat_id=message.chat.id,
#                           message_id=message.message_id + 1)
#                           inline_message_id='2')

# # time.sleep(1)
# # Rabbit
# bot.send_sticker(
#     chat_id=message.chat.id,
#     data='CAACAgIAAxkBAANiYINIK4Bm7D0oxgwL8JAV0roV1NUAAmwCAALc8qsHuunt_I5doFofBA')
# print(message.message_id)
# message.chat.type = 'private'
#
# time.sleep(3)
# # edit_message_text(new_text, chat_id, message_id)
# bot.delete_message(
#     chat_id=message.chat.id,
#     message_id=message.message_id + 1)
# bot.delete_message(
#     chat_id=message.chat.id,
#     message_id=message.message_id)
# message.chat.type = 'private'


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

# start TBot
bot.polling(none_stop=True)

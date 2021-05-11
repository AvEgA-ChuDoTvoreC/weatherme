import os
import random

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telegram_bots.bot_matrix.clients.info import GetUserInfo
from telegram_bots.bot_matrix.matrix.markups import user_keyboard_markup, extra_keyboard_markup, user_keyboard_markup2

STICKER_RED_WOMAN = 'AgADbgIAAtzyqwc'
STICKER_NEO = 'AgADeQIAAtzyqwc'
STICKER_NEO_EVASION = 'AgADaQIAAtzyqwc'
STICKER_MORPHEUS = 'AgADeAIAAtzyqwc'
STICKER_RABBIT = 'AgADbAIAAtzyqwc'
STICKER_TRINITY_HI = 'AgADNwQAAj-VzAo'
STICKER_TRINITY_SHH = 'AgADOAQAAj-VzAo'
STICKER_TRINITY_ADVICE = 'AgADPgQAAj-VzAo'
STICKER_TRINITY_LOVE = 'AgADdQIAAtzyqwc'


class GenerateMarkup:
    def gen_morpheus_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Yes", callback_data="morpheus_yes"),
                   InlineKeyboardButton("No", callback_data="morpheus_no"))
        return markup

    def gen_trinity_markup_club1(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("О чем? 🐇 ", callback_data="trinity_yes1"))
        return markup

    def gen_trinity_markup_club2(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Что такое Матрица? 🐇 ", callback_data="trinity_yes2"))
        return markup

    def gen_trinity_markup_hostel(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Так, это был не сон? 🐇 ", callback_data="trinity_yes3"))
        return markup

    def gen_rabbit_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Пойти за кроликом 🐇 ", callback_data="rabbit_yes"))
        return markup

    def gen_woman_in_red_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(" 🐇 ", callback_data="woman_in_red_yes"))
        return markup

    def gen_again_start_markup(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton(" 🐇 ", callback_data="alarm_yes"),
                   InlineKeyboardButton("No", callback_data="alarm_no"))
        return markup


class MatrixConversation(GenerateMarkup):

    def __init__(self, tbot, tcall=None, tmessage=None):
        self.bot = tbot
        self.call = tcall
        self.message = tmessage

    def answer_help_info(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>Нео:</b>
        /help - help menu
        /start - старт приветствия
        /stop - скрыть доп меню клавиатуры
        /show_my_photo - показать загруженную фотку (либо дефолтную)
        /send_location - отправить свою геолокацию (требуется разрешение в настройках)
        
        <b>поддержка:</b>
        -загрузка фоток
        -отправка геолокации
        -контроль мата
        -обработка присланных стикеров (tip: используй стикеры матрицы)
        
        Have Fun & Good Luck
        """, parse_mode='HTML', reply_markup=user_keyboard_markup())

    def answer_hello(self):
        self.bot.send_message(chat_id=self.message.chat.id,
                              text="""
        Здравствуй, Нео.
        """, parse_mode='markdown')
        self.bot.send_sticker(chat_id=self.message.chat.id,
                              data='CAACAgIAAxkBAAIB52CFEYsUWPehKf8hnXYvRgyEbz2cAAI3BAACP5XMCkLU7Ai1u05wHwQ',
                              reply_markup=self.gen_woman_in_red_markup())

    def answer_weather(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>Нео:</b>
        Мороз и солнце; день чудесный!
        Еще ты дремлешь, друг прелестный —
        Пора, красавица, проснись:
        Открой сомкнуты негой взоры
        Навстречу северной Авроры,
        Звездою севера явись!
        """, parse_mode='HTML', reply_markup=user_keyboard_markup())

    def answer_whoami(self, user_info_dict):
        if user_info_dict:
            self.bot.send_message(chat_id=self.message.from_user.id,
                                  text=f"""
        <b>Агент Смит:</b>
        id:                {user_info_dict.get("id")}
        username:   {user_info_dict.get("username")}
        first_name: {user_info_dict.get("first_name")}
        last_name:  {user_info_dict.get("last_name")}
        """, parse_mode='HTML', reply_markup=user_keyboard_markup())

        else:
            user_info_dict = GetUserInfo(tmessage=self.message).gather_fields()
            self.bot.send_message(chat_id=self.message.from_user.id,
                                  text=f"""
        <b>Агент Смит2:</b>
        id:                {user_info_dict.get("id")}
        username:   {user_info_dict.get("username")}
        first_name: {user_info_dict.get("first_name")}
        last_name:  {user_info_dict.get("last_name")}
        """, parse_mode='HTML', reply_markup=user_keyboard_markup())

    def answer_your_location(self):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        *Координаты:*
        широта: {self.message.location.latitude}
        долгота: {self.message.location.longitude}
        ({self.message.location.latitude},{self.message.location.longitude})
        """, parse_mode='markdown', reply_markup=extra_keyboard_markup())

    def answer_my_position(self):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        *Морфеус:*
        Ты хочешь узнать, что это? Матрица повсюду. 
        Она окружает нас. Даже сейчас она с нами рядом. 
        Ты видишь ее, когда смотришь в окно или включаешь телевизор. 
        Ты ощущаешь ее, когда работаешь, идешь в церковь, 
        когда платишь налоги. 
        Целый мирок, надвинутый на глаза, чтобы спрятать правду.
        
        Что ты только раб, Нео. 
        Как и все, ты с рождения в цепях. С рождения в тюрьме, 
        которой не почуешь и не коснешься. В темнице для разума.
        """, parse_mode='markdown', reply_markup=user_keyboard_markup())
        self.bot.send_location(self.message.from_user.id, '55.727638', '37.619839')

    def answer_morpheus_welcome(self, bot_name, bot_username):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        Наконец-то. Добро пожаловать.
        Как ты уже понял, я - *{bot_name}*.
        (@{bot_username})

        Не знаю, готов ли ты увидеть то, что должен,
        но, увы, у нас время на исходе.

        *Проверь свою клавиатуру на наличие команд*
        Все уже продумали за тебя, Нео.👇
        """, parse_mode='markdown', reply_markup=user_keyboard_markup())

    def answer_empty_with_markup(self, markup):
        self.bot.send_message(self.message.from_user.id,
                              text='...', reply_markup=markup, parse_mode='markdown')

    def stackoverflow(self):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        *Morpheus:*
        Welcome back, Neo!👇
        """, parse_mode='markdown', reply_markup=user_keyboard_markup2())

    def answer_angry(self):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        *Пифия:*
        Мне жаль, малыш, правда, ты добрая душа...
        но нам все таки придется тебя проучить, и, 
        использовать эту ложку не по назначению...
        
        Не расстраивайся. Теперь она будет всегда с тобой и
        будет служить напоминанием о нашей встрече.""", parse_mode='markdown')

    def answer_photo(self):
        #     #all_files = os.listdir(directory)
        #     #random_file = random.choice(all_files)
        #     url = "фото1"
        #     urllib2.urlretrieve(url,'url_image.jpg')
        #     #img = open(directory + '/' + random_file, 'rb')
        img = open('tbot_data/image/marcin-blaszczak.jpg', 'rb')
        self.bot.send_chat_action(self.message.from_user.id, 'upload_photo')
        self.bot.send_photo(
            chat_id=self.message.from_user.id,
            photo=img,
            reply_markup=user_keyboard_markup())
        img.close()

    def answer_heart(self):
        folder = 'tbot_data'
        owner = 'default'
        name = 'love_is'
        all_love_is = os.listdir(os.path.join(folder, owner, name))
        random_file = random.choice(all_love_is)
        filepath = os.path.join(folder, owner, name, random_file)

        love_is = open(filepath, 'rb')
        self.bot.send_chat_action(self.message.from_user.id, 'upload_photo')
        self.bot.send_photo(
            chat_id=self.message.from_user.id,
            photo=love_is,
            reply_markup=extra_keyboard_markup())
        love_is.close()

    def answer_show_uploaded_photo(self):
        folder = 'clients_data'
        owner = str(self.message.from_user.id)
        name = owner + '.jpg'
        filepath = os.path.join(folder, owner, name)

        if os.path.exists(filepath):
            img = open(filepath, 'rb')
            self.bot.send_chat_action(self.message.from_user.id, 'upload_photo')
            self.bot.send_photo(
                chat_id=self.message.from_user.id,
                photo=img,
                reply_markup=extra_keyboard_markup())
            img.close()
        else:
            folder = 'tbot_data'
            owner = 'default'
            name = 'tenor-2' + '.gif'
            filepath = os.path.join(folder, owner, name)

            img = open(filepath, 'rb')
            self.bot.send_chat_action(self.message.from_user.id, 'upload_photo')
            self.bot.send_animation(
                chat_id=self.message.from_user.id,
                animation=img,
                reply_markup=extra_keyboard_markup())
            img.close()

    # def answer_start_car_conversation(self):
    #     msg = self.bot.reply_to(message=self.message,
    #                             text="""\
    #     *Тринити:*
    #     Хорошо, Нео.
    #     Приступим к регистрации твоих данных
    #     в системе!
    #     Отвечай честно, это лишь формальность.
    #
    #     *Твое полное имя?:*
    #     """, parse_mode='markdown', reply_markup=extra_keyboard_markup())
    #     self.bot.register_next_step_handler(msg, self.car_dialog_initial)
    #
    # def car_dialog_initial(self, message):
    #     print("car dialog")
    #     try:
    #         chat_id = message.chat.id
    #         name = message.text
    #         user = User(name)
    #         USER_CAR_INFO_DICT[chat_id] = user
    #         msg = self.bot.reply_to(message=message,
    #                                 text="""
    #     *Твоя фамилия?:*
    #     """, parse_mode='markdown', reply_markup=extra_keyboard_markup())
    #         self.bot.register_next_step_handler(msg, self.process_age_step)
    #     except Exception as e:
    #         self.bot.reply_to(self.message, 'oooops')
    #
    # def process_age_step(self, message):
    #     pass

    def extra_woman_in_red(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAAIDoGCFVBQhliLAE45J-H7htdXCZv2iAAJuAgAC3PKrB6DdpwZCektiHwQ')

    def extra_menu(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>Морфеус:</b>
        Пожалуйста, проходи, садись.
        """, parse_mode='HTML', reply_markup=extra_keyboard_markup())

    def main_menu(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>Морфеус:</b>
        Пожалуйста, проходи, садись.
        """, parse_mode='HTML', reply_markup=user_keyboard_markup())

    def start_questions(self):
        self.bot.delete_message(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id + 1)

        self.bot.send_sticker(chat_id=self.message.chat.id,
                              data='CAACAgIAAxkBAANiYINIK4Bm7D0oxgwL8JAV0roV1NUAAmwCAALc8qsHuunt_I5doFofBA',
                              reply_markup=self.gen_rabbit_markup())

    def rabbit_question(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text="""
        Здравствуй, Нео.
        Меня зовут Тринити.
        Сейчас я могу сказать одно. Ты в опасности. Я здесь, чтобы предупредить.
        """, parse_mode='markdown')

        self.bot.answer_callback_query(self.call.id, "Да, брось. Там прикольно. Вот увидишь.", cache_time='4')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAAIB52CFEYsUWPehKf8hnXYvRgyEbz2cAAI3BAACP5XMCkLU7Ai1u05wHwQ',
                              reply_markup=self.gen_trinity_markup_club1())

    def trinity_question_in_club(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text="""
        Молчи и слушай. Я знаю, почему ты здесь. 
        Знаю, что тебя гнетет. Почему ты не спишь, почему живешь один, 
        и все ночи напролет проводишь за компьютером. 
        Ты ищешь его. 
        Знаю, потому что сама искала. Он нашел меня и объяснил, 
        что я ищу вовсе не его. Что ищу ответ. Нам не дает покоя вопрос, Нео. 
        Он и привел тебя сюда. Ты его задашь, как и я тогда.
        """, parse_mode='markdown')

        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)

        self.bot.answer_callback_query(self.call.id, "За тобой следят, Нео.", cache_time='5')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAAICiWCFJYNCnTcyPsBDGPCtJafJD89eAAI4BAACP5XMCpQbg6Ojk-6iHwQ',
                              reply_markup=self.gen_trinity_markup_club2())

    def trinity_question_in_hostel(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text="""
        (Гостиница Лафейетт)
        """, parse_mode='markdown')

        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)

        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text="""
        *Тринити:* 
        Позволь мне дать тебе один небольшой совет. 
        Будь честным. Он знает больше, чем ты можешь себе представить.
        """, parse_mode='markdown')

        self.bot.answer_callback_query(self.call.id, "Ответ где-то там, Нео. Он тебя ищет.", cache_time='4')

        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAAIC4mCFLUnf_lW0TNXBGcr3cqf37VDiAAI-BAACP5XMCmXGbS9Z4RFmHwQ',
                              reply_markup=self.gen_trinity_markup_hostel())

    def morpheus_question_in_hostel(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text="""
        *Морфеус:*
        Увы, невозможно объяснить, что такое Матрица... 
        Ты должен увидеть это сам. Не поздно отказаться. 
        Потом пути назад не будет. 
        Примешь *синюю* таблетку 💊 - и сказке конец. 
        Ты проснешься в своей постели и поверишь, что это был сон. 
        Примешь *красную* таблетку 💊 - войдешь в страну чудес. 
        Я покажу тебе, глубока ли кроличья нора. 
        Помни, я лишь предлагаю узнать правду, больше ничего.
        """, parse_mode='markdown')

        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 2)

        self.bot.answer_callback_query(self.call.id, "Наконец-то. Добро пожаловать.", cache_time='4')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAANbYINHPGkKa6MZBeuygEKzQJzzp1sAAngCAALc8qsHISNlidiEbn4fBA',
                              reply_markup=self.gen_morpheus_markup())

    def end_questions_yes(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)

        self.bot.answer_callback_query(self.call.id, "*Clock Alarm*", cache_time='5')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)
        self.bot.send_sticker(chat_id=self.call.message.chat.id,
                              data='CAACAgIAAxkBAAIGjGCGugcIGMx888jwvKgIsZt5I3vMAAIiCwACLw_wBt29ccqyC2nmHwQ',
                              reply_markup=self.gen_again_start_markup())

    def delete_one_call(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)

    def delete_two_call(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)
        self.bot.answer_callback_query(callback_query_id=self.call.id,
                                       text="*WELCOME TO REALITY*",
                                       show_alert=True,
                                       cache_time='5')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)

    def delete_one_message(self):
        self.bot.delete_message(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id - 1)

    def delete_two_message(self):
        self.bot.delete_message(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id - 2)
        self.bot.delete_message(
            chat_id=self.message.chat.id,
            message_id=self.message.message_id - 1)

    def show_reality(self):
        try:
            self.bot.send_video(
                chat_id=self.call.message.chat.id,
                data='BAACAgIAAxkBAAIG7GCGx9-Cmrso2vefg0XgMmdLaeXJAAJpDwACGgU4SDZwTDWTm9IBHwQ',
                reply_markup=user_keyboard_markup())
        except Exception as e:
            print(e)
            video_stream = open('tbot_data/video/The_Matrix_(1999)_Welcome_To_The_Real_World.mp4', 'rb')
            self.bot.send_video(
                chat_id=self.call.message.chat.id,
                data=video_stream,
                # data='BAACAgIAAxkBAAIG7GCGx9-Cmrso2vefg0XgMmdLaeXJAAJpDwACGgU4SDZwTDWTm9IBHwQ',
                reply_markup=user_keyboard_markup(),
                width=640, height=640, duration=60
            )
            video_stream.close()



from telegram_bots.bot_weather.clients.info import GetUserInfo
from decouple import config

from telegram_bots.bot_weather.matrix.markups import GenerateMarkup


DJANGO_HOST = config('ENV_DJANGO_HOST', default='0.0.0.0')
DJANGO_PORT = config('ENV_DJANGO_PORT', default='8000')
PROTOCOL = config('ENV_API_PROTOCOL', default='http')


class MessageConversation(GenerateMarkup):

    def __init__(self, t_bot, t_message):
        self.bot = t_bot
        self.message = t_message
        self.bot_name = self.bot.get_me().first_name

    def send_msg(self, message):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=message,
                              parse_mode='HTML',
                              reply_markup=self.user_keyboard_markup())

    def send_fl(self, byte_array):
        self.bot.send_document(chat_id=self.message.from_user.id,
                               data=byte_array,
                               )

    def answer_help_info(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        /help - вызов этого меню
        /start - старт приветствия
        send-my-location - отправить свою геолокацию (требуется разрешение в настройках)
        
        <b>поддержка:</b>
        -отправка геолокации
        -API взаимодействие
        
        HF&GL
        """, parse_mode='HTML', reply_markup=self.user_keyboard_markup())

    def main_menu(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        Пожалуйста, проходи, садись.
        """, parse_mode='HTML', reply_markup=self.user_keyboard_markup())

    def answer_welcome(self):
        self.bot.send_message(chat_id=self.message.chat.id,
                              text=f"""
        {self.bot_name} к твоим услугам!""")

    def answer_api(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        
        """, parse_mode='HTML', reply_markup=self.gen_api_inline_markup())

    def answer_weather(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        Мороз и солнце; день чудесный!
        Еще ты дремлешь, друг прелестный —
        Пора, красавица, проснись:
        Открой сомкнуты негой взоры
        Навстречу северной Авроры,
        Звездою севера явись!
        """, parse_mode='HTML', reply_markup=self.user_keyboard_markup())

    def answer_your_location(self):
        self.bot.send_message(self.message.from_user.id,
                              text=f"""
        *Координаты:*
        широта: {self.message.location.latitude}
        долгота: {self.message.location.longitude}
        ({self.message.location.latitude},{self.message.location.longitude})
        """, parse_mode='markdown', reply_markup=self.user_keyboard_markup())

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


class CallConversation(GenerateMarkup):

    django_protocol_host_port: str = f"{PROTOCOL}://{DJANGO_HOST}:{DJANGO_PORT}"

    def __init__(self, t_bot, t_call):
        self.bot = t_bot
        self.call = t_call
        self.bot_name = self.bot.get_me().first_name

    def main_menu(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        .
        """, parse_mode='HTML', reply_markup=None)

    def call_api_update(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        /api/v1/weather/town/
        """, parse_mode='HTML', reply_markup=self.user_send_town_list())
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        Напишите города через пробел
        для обновления списка.
        Либо выберите шаблонный вариант
        на виртуальной клавиатуре.
        """, parse_mode='HTML')

    def call_api_chose_one(self):
        town_list = """
        1 Moscow
        2 Kazan
        3 Uchai
        4 Saint-Petersburg
        """
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        /api/v1/weather/town/1/
        """, parse_mode='HTML', reply_markup=self.user_show_one_town())
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        Напишите цифру города
        для получения данных.
        {town_list}
        Либо выберите шаблонный вариант
        на виртуальной клавиатуре.
        """, parse_mode='HTML')

    def call_api_chose_many(self):
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        <b>{self.bot_name}:</b>
        /api/v1/weather/town/1/5/
        """, parse_mode='HTML', reply_markup=self.user_show_many_towns())
        self.bot.send_message(chat_id=self.call.message.chat.id,
                              text=f"""
        do something
        """, parse_mode='HTML')

    def delete_one_call(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)

    def delete_two_call(self):
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id - 1)
        # self.bot.answer_callback_query(callback_query_id=self.call.id,
        #                                text="*WELCOME TO REALITY*",
        #                                show_alert=True,
        #                                cache_time='5')
        self.bot.delete_message(
            chat_id=self.call.message.chat.id,
            message_id=self.call.message.message_id)

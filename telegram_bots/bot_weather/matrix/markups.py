from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


class GenerateMarkup:
    @staticmethod
    def gen_api_inline_markup():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("update_town_list", callback_data="update_town_list"),
                   InlineKeyboardButton("chose_one_town", callback_data="chose_one_town"),
                   InlineKeyboardButton("chose_many_towns", callback_data="chose_many_towns"))
        return markup

    @staticmethod
    def gen_weather_inline_markup():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Weather 🐇 ", callback_data="weather"))
        return markup

    @staticmethod
    def gen_main_menu_inline_markup():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Menu", callback_data="menu"))
        return markup

    @staticmethod
    def gen_town_list():
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Moscow", callback_data="menu"))
        return markup

    @staticmethod
    def user_keyboard_markup():
        user_markup = ReplyKeyboardMarkup(True, False)
        button_geo = KeyboardButton(text="send-my-location", request_location=True)
        user_markup.row('/start', '/help')
        user_markup.row('погода', 'API')
        user_markup.add(button_geo)
        return user_markup

    @staticmethod
    def user_api_keyboard_markup():
        user_markup = ReplyKeyboardMarkup(True, False)
        user_markup.row('/tt')
        user_markup.row('/pp', '/ss')
        return user_markup

    @staticmethod
    def user_send_town_list():
        user_markup = ReplyKeyboardMarkup(True, False)
        button_geo = KeyboardButton(text="send-default-towns")
        user_markup.add(button_geo)
        return user_markup

    @staticmethod
    def user_show_one_town():
        user_markup = ReplyKeyboardMarkup(True, False)
        button_geo = KeyboardButton(text="send-default-number")
        user_markup.add(button_geo)
        return user_markup

    @staticmethod
    def user_show_many_towns():
        user_markup = ReplyKeyboardMarkup(True, False)
        button_geo = KeyboardButton(text="send-default-range")
        user_markup.add(button_geo)
        return user_markup


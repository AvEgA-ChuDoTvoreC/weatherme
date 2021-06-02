from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def user_keyboard_markup():
    user_markup = ReplyKeyboardMarkup(True, True)
    # button_geo = KeyboardButton(text="/location", request_location=True)
    user_markup.row('/start', '/help', '/stop')
    user_markup.row('привет', 'кто я?', 'где мы?')
    user_markup.row('погода', 'фото', '... ->')
    # user_markup.row('фото', 'аудио', 'документы')
    # user_markup.row('стикер', 'видео', 'голос', 'локация')
    # user_markup.add(button_geo)
    return user_markup


def user_keyboard_markup2():
    user_markup = ReplyKeyboardMarkup(True, True)
    button_site = KeyboardButton(text="Web site 🌐", request_location=True)

    user_markup.row('/start', '/help', '/stop')
    user_markup.row('📇', '📉', '💻')
    user_markup.add(button_site)
    return user_markup


def extra_keyboard_markup():
    extra_markup = ReplyKeyboardMarkup(True, True)
    button_geo = KeyboardButton(text="/send_location", request_location=True)
    # button_photo = KeyboardButton(text="/send_photo", request_location=True)
    button_help = KeyboardButton(text="/show_my_photo")
    extra_markup.add(button_geo)
    # extra_markup.add(button_photo)
    extra_markup.add(button_help)
    extra_markup.row('💕️', 'назад', '🚘')
    # extra_markup.row('x', 'x')

    return extra_markup


# def location_markup():
#     keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = KeyboardButton(text="/location", request_location=True)
#     keyboard.add(button_geo)
#     return keyboard

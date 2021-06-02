
STICKER_RED_WOMAN = 'AgADbgIAAtzyqwc'
STICKER_NEO = 'AgADeQIAAtzyqwc'
STICKER_NEO_EVASION = 'AgADaQIAAtzyqwc'
STICKER_MORPHEUS = 'AgADeAIAAtzyqwc'
STICKER_RABBIT = 'AgADbAIAAtzyqwc'
STICKER_TRINITY_HI = 'AgADNwQAAj-VzAo'
STICKER_TRINITY_SHH = 'AgADOAQAAj-VzAo'
STICKER_TRINITY_ADVICE = 'AgADPgQAAj-VzAo'
STICKER_TRINITY_LOVE = 'AgADdQIAAtzyqwc'


class StickerRelpy:

    def __init__(self, tbot, tcall=None, tmessage=None):
        self.bot = tbot
        self.call = tcall
        self.message = tmessage

    def compare_sticker_with(self, sticker):
        if self.message.sticker.file_unique_id == sticker:
            if sticker == STICKER_NEO:
                self.agent_smith()
            elif sticker == STICKER_TRINITY_LOVE:
                self.trinity_love()

    def trinity_love(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text="""
        *Тринити:* 
        Нео, я больше не боюсь. 
        Провидица предсказала мне, что я должна влюбиться. 
        И мой любимый - Избранный.
        """, parse_mode='markdown')

    def agent_smith(self):
        self.bot.send_message(chat_id=self.message.from_user.id,
                              text="""
        *Агент Смит:* 
        Как вы видите, мы за Вами давненько наблюдаем, мистер Андерсон. 
        Оказывается Вы живете двойной жизнью. 
        В одной жизни Вы - Томас А. Андерсон, 
        программист в крупной уважаемой компании. 
        У Вас есть медицинская страховка, Вы платите налоги и еще - 
        помогаете консьержке выносить мусор. 
        Другая Ваша жизнь - в компьютерах. 
        И тут Вы известны как хакер Нео. Вы виновны практически во 
        всех уголовно наказуемых компьютерных преступлениях. 
        У первого - Томаса - есть будущее. 
        У Нео - нет. 
        Буду предельно откровенен с Вами, мистер Андерсон. 
        Вы здесь, потому что нам нужна помощь. 
        Мы знаем, что с Вами вошел в контакт один субъект, 
        известный под кличкой Морфеус. 
        Кем Вы его вообразили - несущественно. 
        Власти многих стран называют его опаснейшим преступником. 
        Мои коллеги думают, что я зря теряю с Вами время, но я верю, 
        Вы исполните свой гражданский долг. Мы готовы уничтожить досье, 
        дать Вам шанс. От Вас нужно только одно - помогите обезвредить 
        известного террориста.
        """, parse_mode='markdown')

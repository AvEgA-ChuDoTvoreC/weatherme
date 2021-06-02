

class GetUserInfo:
    def __init__(self, t_message):
        self.message = t_message
        self.user_username = None
        self.user_first_name = None
        self.user_last_name = None
        self.user_id = None
        self.user_is_bot = None
        self.user_dict = None

    def gather_fields(self) -> dict:
        """
        Gather User info into [dict]
        :return: dict
        """
        self.user_id = str(self.message.from_user.id)
        self.user_username = self.message.from_user.username
        self.user_first_name = self.message.from_user.first_name
        self.user_last_name = self.message.from_user.last_name
        self.user_is_bot = self.message.from_user.is_bot
        self.user_dict = {
            "id": self.user_id,
            "username": self.user_username,
            "first_name": self.user_first_name,
            "last_name": self.user_last_name,
            "is_bot": self.user_is_bot
        }

        return self.user_dict


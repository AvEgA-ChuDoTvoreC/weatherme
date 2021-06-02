

class CarUser:
    def __init__(self, user_id, user_nickname, name):
        self.user_id = user_id
        self.user_nick = user_nickname

        self.name = name
        self.surname = None
        self.lastname = None
        self.age = None
        self.sex = None

        self.city = None
        self.car_certificate_of_registration_number = None
        self.car_number = None
        self.car_vin = None
        self.car_model = None
        self.car_type = None
        self.car_manufacture_year = None
        self.car_color = None
        self.car_engine_power = None
        self.car_passport_number = None
        self.car_weight_max = None
        self.car_weight_min = None

        self.car_driver_license_number = None
        self.car_driver_license_start_date = None
        self.car_driver_license_end_date = None
        self.car_driver_license_categories = None


class GetUserInfo:
    def __init__(self, tmessage):
        self.message = tmessage
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


class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print("First name:", self.__first_name,
              "\nLast name:", self.__last_name,
              "\nUsername:", self.__username,
              "\nEmail:", self.__email,
              "\nPassword:", self.__password,
              "\n"
              )

    def save_user(self):
        # f = open("db.txt", "a")
        # f.write(self.__first_name + '#' +
        #         self.__last_name + '#' +
        #         self.__username + '#' +
        #         self.__email + '#' +
        #         self.__password + '\n'
        #         )
        # f.close()
        user = self.__dict__.values()
        with open('db.txt', 'a') as db_file:
            db_file.write("#".join(user)+"\n")

    @staticmethod
    def get_all_users():
        users = []
        with open('db.txt') as db_file:
            for line in db_file:
                if len(line.strip()) > 0:  # ігнорим пусті строки файла
                    user = line.strip()
                    user_properties = user.split("#")
                    users.append(user_properties)
        return users

    def register(self):
        """1. Реєстрація нового користувача з перевіркою (перевірити чи користувач вже є в файлі)
        """
        user = self.__dict__.values()
        all_users = self.get_all_users()
        for item in all_users:
            if item[2] == self.__username:
                print("Username '" + item[2] + "' is already present")
                return
        with open('db.txt', 'a') as db_file:
            db_file.write("#".join(user)+"\n")

    @classmethod
    def login(cls, login, password):
        """ 2. Логін користувача (логін по username з перевіркою паролю.)
        """
        all_users = cls.get_all_users()
        for item in all_users:
            # if username is the same, return pass == pass
            if item[2] == login:
                return item[4] == password
        # if no such username in file
        return False

    @classmethod
    def remove(cls, login):
        """3. Видалення користувача (по username)
        """
        removed = False
        all_users = cls.get_all_users()

        with open('db.txt', 'w') as db_file:
            for item in all_users:
                if item[2] != login:
                    db_file.write("#".join(item)+"\n")
                else:
                    removed = True
        return removed

    def menu(self):
        pass

class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password
        # self.

    def show_user_info(self):
        print("First name:", self.__first_name,
              "\nLast name:", self.__last_name,
              "\nUsername:", self.__username,
              "\nEmail:", self.__email,
              "\nPassword:", self.__password,
              "\n"
              )

    def save_user(self):
        # user = []
        # user.append(self.__first_name)
        # user.append(self.__last_name)
        # user.append(self.__username)
        # user.append(self.__email)
        # user.append(self.__password)

        f = open("db.txt", "a")
        f.write(self.__first_name + '#' +
                self.__last_name + '#' +
                self.__username + '#' +
                self.__email + '#' +
                self.__password + '\n'
                )
        f.close()

        # with open('db.txt','a') as db_file:
        #     db_file.write(", ".join(user)+"\n")
    def show_all_users(self):
        users = []
        with open('db.txt') as db_file:
            for line in db_file:
                if len(line.strip()) > 0:  # ігнорим пусті строки файла
                    user = line.strip()
                    user_properties = user.split("#")
                    users.append(user_properties)
        return users

    def login(self):
        pass

    def menu(self):
        pass

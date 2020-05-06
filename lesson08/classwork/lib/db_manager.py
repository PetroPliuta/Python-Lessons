import mysql.connector


class Db_manager:
    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        # print(self.__db)
        self.__cursor = self.__db.cursor()
        self.__cursor.execute(
            "CREATE DATABASE if not exists `python_lesson08`;")
        self.__cursor.execute("use `python_lesson08`")
        self.__cursor.execute(
            "CREATE TABLE if not exists users (id INT AUTO_INCREMENT PRIMARY KEY, username varchar(255), email varchar(255), password varchar(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n"))
            if choice == 1:
                print("register")
                self.__register()
            elif choice == 2:
                print("Login")
                logged_in = self.__login()
                print("Logged in:", logged_in)
            elif choice == 4:
                print("Delete by login")
                self.__delete()
            elif choice == 0:
                print("Exit")
                exit = True
            else:
                print("Wrong choice")

    def __register(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        re_password = input("Retype password: ")
        if password != re_password:
            print("Passwords do not match")
            return
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='"+username+"'")
        result = self.__cursor.fetchone()
        # print("Result from db: ", result)
        if result != None:
            print("User exists")
            return
        self.__cursor.execute(
            "INSERT INTO users (username, email, password) VALUES ('%s', '%s', '%s')" % (username, email, password))
        self.__db.commit()

    def __delete(self):
        username = input("Enter login: ")
        self.__cursor.execute(
            "DELETE FROM users WHERE username='"+username+"'")
        # result = self.__cursor.fetchone()
        # print(result)
        self.__db.commit()
        print(self.__cursor.rowcount, "record(s) deleted")
        # print(type(self.__cursor.rowcount))

        # result = self.__cursor.fetchone()

    def __login(self):
        username = input("Enter login: ")
        password = input("Enter password: ")
        self.__cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = %s && password = %s", (username, password))
        result = self.__cursor.fetchone()
        print("Login result:", result)

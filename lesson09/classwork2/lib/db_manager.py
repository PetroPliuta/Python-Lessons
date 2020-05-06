import mysql.connector
import requests
from lib.settings import COVID19_URL


class Db_manager:
    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute(
            "CREATE DATABASE if not exists `python_lesson09`;")
        self.__cursor.execute("use `python_lesson09`")
        self.__cursor.execute(
            "CREATE TABLE if NOT EXISTS Global (id int auto_increment primary key, NewConfirmed int, TotalConfirmed int, NewDeaths int, TotalDeaths int, NewRecovered int, TotalRecovered int);")
        self.__cursor.execute(
            "CREATE TABLE if NOT EXISTS Countries (id int auto_increment primary key, Country varchar(255), CountryCode varchar(12),Slug varchar(255), NewConfirmed int, TotalConfirmed int, NewDeaths int, TotalDeaths int, NewRecovered int, TotalRecovered int, Date varchar(255));")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n0. Exit\n"))
            if choice == 1:
                print("Update")
                self.__update_covid_data()
            elif choice == 2:
                print("Login")
                logged_in = self.__login()
                print("Logged in:", logged_in)
            elif choice == 3:
                print("Edit")
                self.__edit()
            elif choice == 4:
                print("Delete by login")
                self.__delete()
            elif choice == 5:
                print("Show all")
                self.__show_all()
            elif choice == 6:
                print("Search by login")
                self.__search_by_username()
            elif choice == 7:
                print("Search by email")
                self.__search_by_email()
            elif choice == 0:
                print("Exit")
                exit = True
            else:
                print("Wrong choice")

    def __update_covid_data(self):
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()
        # print(covid_data['Global'])
        # print(covid_data['Countries'])
        for item in covid_data['Countries']:
            print(item)
            self.__cursor.execute(
                "INSERT INTO Countries (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'], item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date']))
            self.__db.commit()

    # def __register(self):
    #     username = input("Enter username: ")
    #     email = input("Enter email: ")
    #     password = input("Enter password: ")
    #     re_password = input("Retype password: ")
    #     if password != re_password:
    #         print("Passwords do not match")
    #         return
    #     self.__cursor.execute(
    #         "SELECT * FROM users WHERE username='"+username+"'")
    #     result = self.__cursor.fetchone()
    #     if result != None:
    #         print("User exists")
    #         return
    #     self.__cursor.execute(
    #         "INSERT INTO users (username, email, password) VALUES ('%s', '%s', '%s')" % (username, email, password))
    #     self.__db.commit()

    def __delete(self):
        username = input("Enter login: ")
        self.__cursor.execute(
            "DELETE FROM users WHERE username='"+username+"'")
        self.__db.commit()
        print(self.__cursor.rowcount, "record(s) deleted")

    def __login(self):
        username = input("Enter login: ")
        password = input("Enter password: ")
        self.__cursor.execute(
            "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s", (username, password))
        result = self.__cursor.fetchone()
        return result[0] > 0

    def __edit(self):
        """username, email, password"""
        username = input("Enter login: ")
        self.__cursor.execute(
            "SELECT id FROM users WHERE username = '"+username+"'")
        result = self.__cursor.fetchone()
        if result == None:
            print("No such user")
            return
        choice = input(
            "Enter edit field\n1. Username\n2. Email\n3. Password\n0. Exit\n")
        if choice == '1':
            new_username = input("Enter new username: ")
            self.__cursor.execute(
                "UPDATE users SET username = '"+new_username+"' WHERE username = '"+username+"'")
        elif choice == '2':
            new_email = input("Enter new email: ")
            self.__cursor.execute(
                "UPDATE users SET email = '"+new_email+"' WHERE username = '"+username+"'")
        elif choice == '3':
            new_password = input("Enter new password: ")
            self.__cursor.execute(
                "UPDATE users SET password = '"+new_password+"' WHERE username = '"+username+"'")
        elif choice == '0':
            print('Exit')
            return
        else:
            print('Error')
            return
        self.__db.commit()
        print("Edit OK")

    def __show_all(self):
        self.__cursor.execute("SELECT `username`, `email` FROM `users`")
        result = self.__cursor.fetchall()
        print("-"*20)
        print("Username | Email")
        for user in result:
            print(user[0], " | ", user[1])
        print("-"*20)

    def __search_by_username(self):
        username = input("Enter login: ")
        search = "SELECT username, email FROM users WHERE username LIKE '%"+username+"%'"
        self.__cursor.execute(search)
        result = self.__cursor.fetchall()
        print("-"*20)
        if len(result) == 0:
            print("User not found")
        else:
            print("Username | Email")
            for user in result:
                print(user[0], " | ", user[1])
        print("-"*20)

    def __search_by_email(self):
        email = input("Enter email: ")
        search = "SELECT username, email FROM users WHERE email LIKE '%"+email+"%'"
        self.__cursor.execute(search)
        result = self.__cursor.fetchall()
        print("-"*20)
        if len(result) == 0:
            print("User not found")
        else:
            print("Username | Email")
            for user in result:
                print(user[0], " | ", user[1])
        print("-"*20)

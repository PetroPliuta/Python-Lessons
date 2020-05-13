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
        self.__cursor = self.__db.cursor(dictionary=True)
        self.__cursor.execute(
            "CREATE DATABASE if not exists `python_lesson09`;")
        self.__cursor.execute("use `python_lesson09`")
        self.__cursor.execute(
            "CREATE TABLE if NOT EXISTS Global (id int auto_increment primary key, NewConfirmed int, TotalConfirmed int, NewDeaths int, TotalDeaths int, NewRecovered int, TotalRecovered int, Date DATETIME);")
        self.__cursor.execute(
            "CREATE TABLE if NOT EXISTS Countries (id int auto_increment primary key, Country varchar(255), CountryCode varchar(12), Slug varchar(255), NewConfirmed int, TotalConfirmed int, NewDeaths int, TotalDeaths int, NewRecovered int, TotalRecovered int, Date DATETIME);")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. Search by country name\n3. Search by country code\n4. Top 10 (TotalConfirmed)\n5. Top 10 (TotalRecovered)\n0. Exit\n"))
            if choice == 1:
                print("Update")
                self.__update_covid_data()
            elif choice == 2:
                print("Search by country name")
                self.__search_by_country_name()
            elif choice == 3:
                print("Search by country code")
                self.__search_by_country_code()
            elif choice == 4:
                print("Top 10 (TotalConfirmed)")
                self.__total_confirmed()
            elif choice == 5:
                print("Top 10 (TotalRecovered)")
                self.__total_recovered()
            elif choice == 0:
                print("Exit")
                exit = True
            else:
                print("Wrong choice")

    def __update_covid_data(self):
        """1. Update covid database"""
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()

        # Global
        global_ = covid_data['Global']
        query = """ INSERT INTO Global (NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s',
                STR_TO_DATE("%s",'%%Y-%%m-%%dT%%TZ'))
        """ % (global_["NewConfirmed"], global_["TotalConfirmed"], global_["NewDeaths"], global_["TotalDeaths"], global_["NewRecovered"], global_["TotalRecovered"], covid_data['Date'])
        self.__cursor.execute("TRUNCATE TABLE Global;")
        self.__cursor.execute(query)

        # Countries
        self.__cursor.execute("TRUNCATE TABLE Countries;")
        for item in covid_data['Countries']:
            query = """
            INSERT INTO Countries (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", STR_TO_DATE("%s",'%%Y-%%m-%%dT%%TZ'))
            """ % (item['Country'], item['CountryCode'], item['Slug'], item['NewConfirmed'], item['TotalConfirmed'], item['NewDeaths'], item['TotalDeaths'], item['NewRecovered'], item['TotalRecovered'], item['Date'])
            self.__cursor.execute(query)
        self.__db.commit()

    def __search_by_country_name(self):
        """2. Показати інформацію по назві країни (Ukraine)"""
        country = input("Enter country name (Ukraine): ")
        self.__cursor.execute(
            "SELECT Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date FROM Countries WHERE Country='"+country+"'")
        result = self.__cursor.fetchone()
        if result == None:
            print("Country '"+country+"' not found")
            return
        # print(result)
        print("-"*10+" Country info "+"-"*10)
        for item in result:
            print(item, ": ", result[item], sep="")
        print("-"*30)

    def __search_by_country_code(self):
        """3. Показати інформацію по коду країни (UA)"""
        code = input("Enter country code (UA): ")
        self.__cursor.execute(
            "SELECT Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date FROM Countries WHERE CountryCode='"+code+"'")
        result = self.__cursor.fetchone()
        if result == None:
            print("Country with code '"+code+"' not found")
            return
        # print(result)
        print("-"*10+" Country info "+"-"*10)
        for item in result:
            print(item, ": ", result[item], sep="")
        print("-"*33)

    def __total_confirmed(self):
        """"""
        self.__cursor.execute(
            "SELECT Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date FROM Countries ORDER BY TotalConfirmed DESC LIMIT 10")
        result = self.__cursor.fetchall()

        print("-"*140)
        print("%-30s| %-5s| %-20s| %-8s| %-8s| %-10s| %-12s| %-12s| %-14s| %-20s" %
              ("Country", "Code", "Slug", "New", "Total", "NewDeaths",
               "TotalDeaths", "NewRecovered", "TotalRecovered", "Date")
              )
        print("-"*140)

        for country in result:
            print("%-30s| %5s| %-20s| %8s| %8s| %10s| %12s| %12s| %14s| %20s" %
                  (country['Country'], country['CountryCode'], country['Slug'], country['NewConfirmed'],
                   country['TotalConfirmed'], country['NewDeaths'], country['TotalDeaths'], country['NewRecovered'],
                   country['TotalRecovered'], country['Date']))
        print("-"*140)

    def __total_recovered(self):
        self.__cursor.execute(
            "SELECT Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date FROM Countries ORDER BY TotalRecovered DESC LIMIT 10")
        result = self.__cursor.fetchall()

        print("-"*140)
        print("%-30s| %-5s| %-20s| %-8s| %-8s| %-10s| %-12s| %-12s| %-14s| %-20s" %
              ("Country", "Code", "Slug", "New", "Total", "NewDeaths",
               "TotalDeaths", "NewRecovered", "TotalRecovered", "Date")
              )
        print("-"*140)

        for country in result:
            print("%-30s| %5s| %-20s| %8s| %8s| %10s| %12s| %12s| %14s| %20s" %
                  (country['Country'], country['CountryCode'], country['Slug'], country['NewConfirmed'],
                   country['TotalConfirmed'], country['NewDeaths'], country['TotalDeaths'], country['NewRecovered'],
                   country['TotalRecovered'], country['Date']))
        print("-"*140)

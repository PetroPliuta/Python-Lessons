#!/usr/bin/python3.8
# import mysql.connector
from lib.db_manager import Db_manager
from lib.settings import *

m = Db_manager(HOST, USERNAME, PASSWORD)

m.menu()


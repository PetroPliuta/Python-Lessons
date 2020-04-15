from lib.person import Users

user = Users("John", "Snow", "jsnow", "e@ma.il", "pa$$word")
# user.show_user_info()
# user.save_user()

# user2 = Users("John", "Doe", "Snow", "mail", 'pass')
# user2.save_user()

print(user.show_all_users())

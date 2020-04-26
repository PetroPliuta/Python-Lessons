from lib.person import Users

# До роботи яку робили в класі доробити:
# 1. Реєстрацію нового користувача з перевіркою (перевірити чи коистувач вже є в файлі)

user = Users("John", "Snow", "jsnow", "e@ma.il", "pa$$word")
user.register()

user = Users("John", "Snow", "jsnow4", "e@ma.il", "pa$$word")
user.register()

# 2. Логін користувача (логін по username з перевіркою паролю.)

print("User logged in:", Users.login("jsnow", "pass"))
print("User logged in:", Users.login("jsnow2", "pass"))
print("User logged in:", Users.login("jsnow", "pa$$word"))

# 3. Видалення користувача (по username)

result = Users.remove("")
print("User was removed:", result)

result = Users.remove("jsnow3")
print("User was removed:", result)

result = Users.remove("jsnow")
print("User was removed:", result)

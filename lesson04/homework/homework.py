"""1.Написати клас "Карточка на знижку" (DiscountCard), який містить наступну інформацію: 

Номер карточки 
Розмір знижки (знижка передбачається накопичуваною; на початковому етапі вона рівна 1%. За кожні 1000 грн. покупки, сума знижки збільшується на 1%.) 
Приховане допоміжне поле для збереження вартості накупленого товару 
Дата видачі карточки в форматі "12/02/1200") 
Забезпечити можливість: 
Купляти товар з використанням карточки на знижку; 
Виводити інформацію про поточну величину знижки; 
Виводити інформацію про те, на яку суму ще необхідно докупити товару, щоб величина знижки збільшилась. 
"""
import random


class DiscountCard:
    # TODO: get date default value form function
    def __init__(self, *, date="01/01/2020", amount=0):
        self.__card_number = random.randint(100000, 999999)
        self.__discount = 1
        self.__amount = 0  # вартість накупленого товару

        if self.__check_date(date):
            self.__date = date
        else:
            self.__date = "01/01/2020"

        if amount != 0:
            self.__add_money(amount)

    def __check_date(self, date):
        """Перевірка дати на відповіднісь типу str і значення формату date/month/year"""
        if type(date) == str:
            result = date.strip().split("/")
            if len(result) == 3 and self.__check_int(result[0]) and self.__check_int(result[1]) and self.__check_int(result[2]):
                if 1 <= int(result[0]) <= 31 and 1 <= int(result[1]) <= 12:
                    return True
            else:
                return False
        else:
            return False

    def __add_money(self, amount):
        """Додавання грошей на рахунок і перерахунок знижки"""
        if self.__check_float(amount) and float(amount) > 0:
            self.__amount += float(amount)
            self.__discount = 1 + self.__amount // 1000

    def __str__(self):
        return "Discount Card: #"+str(self.__card_number)+", discount: "+str(self.__discount)+"%, date: "+str(self.__date)

    def __check_float(self, amount):
        """Перевірка чи можна конвертувати отримане значення в число (float)"""
        try:
            float(amount)
        except ValueError:
            return False
        else:
            return True

    def __check_int(self, amount):
        """Перевірка чи можна конвертувати отримане значення в число (int)"""
        try:
            int(amount)
        except ValueError:
            return False
        else:
            return True

    def buy_goods(self, amount):
        """Купляти товар з використанням карточки на знижку"""
        if self.__check_float(amount):
            self.__add_money(amount)

    def print_discount(self):
        """Виводити інформацію про поточну величину знижки"""
        print("Current discount: ", self.__discount, "%", sep="")

    def print_required_amount_to_increase_discount(self):
        """Виводити інформацію про те, 
        на яку суму ще необхідно докупити товару, 
        щоб величина знижки збільшилась. 
        """
        print("Щоб величина знижки збільшилась, ще необхідно докупити товару на суму:",
              1000 - self.__amount % 1000)


card1 = DiscountCard(amount="123")
card2 = DiscountCard(amount=23, date="12/03/2024")
print(card1, card2, sep="\n")
print("="*40)  # ========================================
card1.buy_goods("1234")
card1.print_discount()
print(card1)
card1.print_required_amount_to_increase_discount()

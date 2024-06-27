class Mentor:
    def __init__(self, first_name, last_name, age, address, email, mentoring_group, learning_group):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.email = email
        self.mentoring_group = mentoring_group
        self.learning_group = learning_group
        self.coins = 0

    def add_coins(self, amount):
        if amount > 0:
            self.coins += amount
            print(f"{amount} коинов добавлено. Текущий баланс: {self.coins}")
        else:
            print("Сумма должна быть больше 0.")

    def withdraw_coins(self, amount):
        if 0 < amount <= self.coins:
            self.coins -= amount
            print(f"{amount} коинов снято. Текущий баланс: {self.coins}")
        else:
            print("Недостаточно средств или некорректная сумма.")

    def __str__(self):
        return (f"Ментор: {self.first_name} {self.last_name}\n"
                f"Возраст: {self.age}\n"
                f"Адрес: {self.address}\n"
                f"Email: {self.email}\n"
                f"Группа менторства: {self.mentoring_group}\n"
                f"Группа обучения: {self.learning_group}\n"
                f"Баланс коинов: {self.coins}")
  
mentor1 = Mentor("aslan", "baybalaev", 16, "г. Osh, ул. Iminjan zakirova, д. 160", "asalan@gmail.com", "15.1b", "18.1b")
print(mentor1)

mentor1.add_coins(50)
mentor1.withdraw_coins(20)
mentor1.withdraw_coins(40)

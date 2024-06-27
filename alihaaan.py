import sqlite3

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        full_name VARCHAR(100),
        age INT,
        addres VARCHAR(100),
        email TEXT,
        which_month INT,
        geeks_coin INT
    );
""")

class Geek_coin:
    def __init__(self):
        self.full_name = None
        self.age = 0
        self.addres = None
        self.email = None
        self.which_month = 0
        self.geeks_coin = 0
        
    def register(self, full_name, age, addres, email, which_month):
        self.full_name = full_name
        self.age = age
        self.addres = addres
        self.email = email
        self.which_month = which_month
        cursor.execute('''
            INSERT INTO students (full_name, age, addres, email, which_month, geeks_coin)
            VALUES (?, ?, ?, ?, ?, 0)
        ''', (full_name, age, addres, email, which_month))
        connect.commit()
        
    def plus_coin(self, amount, mentor_name):
        cursor.execute('SELECT * FROM students WHERE full_name = ?', (mentor_name,))
        student = cursor.fetchone()
        if student:
            cursor.execute('UPDATE students SET geeks_coin = geeks_coin + ? WHERE full_name = ?', (amount, mentor_name))
            connect.commit()
            self.geeks_coin += amount
        else:
            print(f'Ментор с именем "{mentor_name}" не найден в базе данных.')

    def minus_coin(self, amount, mentor_name):
        cursor.execute('SELECT * FROM students WHERE full_name = ?', (mentor_name,))
        student = cursor.fetchone()
        if student:
            cursor.execute('UPDATE students SET geeks_coin = geeks_coin - ? WHERE full_name = ?', (amount, mentor_name))
            connect.commit()
            self.geeks_coin -= amount
        else:
            print(f'Ментор с именем "{mentor_name}" не найден в базе данных.')

    def main(self):
        while True:
            print('Выберите вариант: ')
            you = int(input('1 = Регистрация, 2 = добавить коин, 3 = отнять коин: '))
            if you == 1:
                full_name = input("Введите имя: ")
                age = int(input("Введите ваш возраст: "))
                addres = input("Введите адрес: ")
                email = input("Введите почту: ")
                which_month = int(input("Введите ваш месяц обучения: "))
                self.register(full_name, age, addres, email, which_month)
                
            elif you == 2:
                mentor_name = input('Введите имя ментора: ')
                if mentor_name:
                    amount = int(input('Сколько коинов вы хотите добавить: '))
                    self.plus_coin(amount, mentor_name)
                else:
                    print('Такого ментора нет')
                    
            elif you == 3:
                mentor_name = input('Введите имя ментора: ')
                amount = int(input('Сколько коинов вы хотите отнять: '))
                self.minus_coin(amount, mentor_name)
                
            else:
                print('Такой команды нет!')
                    
mentor1 = Geek_coin()
mentor1.main()

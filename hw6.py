import random


class Random_game:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.secret_number = random.randint(lower_bound, upper_bound)
        self.guesses = 0

    def random_game(self, guess):
        self.guesses += 1
        if guess < self.secret_number:
            return "Ваше число меньше загаданного."
        elif guess > self.secret_number:
            return "Ваше число больше загаданного."
        else:
            return f"Поздравляем! Вы угадали число {self.secret_number} за {self.guesses} попыток."

    def reset_game(self):
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.guesses = 0


if __name__ == "__main__":
    game = Random_game(1, 100)
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    while True:
        guess = int(input("Введите ваше предположение: "))
        result = game.random_game(guess)
        print(result)
        if "Поздравляем" in result:
            play_again = input("Хотите сыграть еще раз? (да/нет): ")
            if play_again.lower() == "да":
                game.reset_game()
                print("Игра перезапущена. Я снова загадал число от 1 до 100.")
            else:
                print("Спасибо за игру! До свидания!")
                break

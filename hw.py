def main():
    user_input = input("Введите число: ")
    
    try:
        number = int(user_input)
        print(f"Вы ввели число: {number}")
    except ValueError:
        print("Ошибка: введенная строка не является числом.")

main()

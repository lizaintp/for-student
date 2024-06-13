# from typing import Any


# class MagicCalculator:
#     def __init__ (self , number1, number2 ):
#         self.number1 = number1
#         self.number2 = number2

#     def __add__ (self,other):
#         return self.number1 + other.number1, self.number2 + other.number2
    
#     def __sub__(self,other):
#         return self.number1 - other.number1, self.number2 - other.number2
    
#     def __mul__(self,other):
#         return self.number1 * other.number1, self.number2 * other.number2
    
#     def __truediv__(self,other):
#         return self.number1 / other.number1, self.number2 / other.number2

#     def __floordiv__(self,other):
#         return self.number1 // other.number1, self.number2 // other.number2
    
#     def __eq__(self,other):
#         return self.number1 == other.number1, self.number2 == other.number2



# num1 = MagicCalculator(12315,21424)
# num2 = MagicCalculator(125, 2131)
# print(num1+num2)
# print(num1-num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 == num2)

class Book:
    def __init__(self, autor , year, book):
        self.autor = autor
        self.year = year
        self.book = book

    def __str__(self):
        return f"Автор: {self.autor}, год: {self.year}, название: {self.book}"
    
    def __eg__(self, other):
        return self.year == other.year
    
    def __lt__(self, other):
        return self.year < other.year
    
    def __le__(self, other):
        return self.year <= other.year   
    
    def __gt__(self, other):
        return self.year > other.year
    
    def __ge__(self, other):
        return self.year >= other.year
    
    def __ne__(self, other):
        return self.year != other.year
    
       
pushkin = Book('Pushkin', 1982, 'Золотая рыбка')
levtolstoy = Book("LevToLstoy", 1982, "Война и Мир")
print(pushkin)
print(levtolstoy)
print(pushkin.year==levtolstoy.year)
print(pushkin.year<levtolstoy.year)
print(pushkin.year<=levtolstoy.year)
print(pushkin.year>levtolstoy.year)
print(pushkin.year>=levtolstoy.year)
print(pushkin.year!=levtolstoy.year)

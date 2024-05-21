# class MagicCalculator:
#     def __init__(self, namber1, namber2):
#         self.namber1 = namber1
#         self.namber2 = namber2

#     def __add__ (self,other):
#         return self.namber1+other.namber1, self.namber2+other.namber2
    
#     def __sub__ (self,other):
#         return self.namber1-other.namber1, self.namber2-other.namber2
    
#     def __mul__ (self,other):
#         return self.namber1*other.namber1, self.namber2*other.namber2
    
#     def __truediv__ (self,other):
#         return self.namber1/other.namber1, self.namber2/other.namber2
    
#     def __floordiv__ (self,other):
#         return self.namber1//other.namber1, self.namber2//other.namber2
    
# nam1 = MagicCalculator(10,11)
# nam2 = MagicCalculator(25,53)
# print(nam1+nam2)
# print(nam1-nam2)
# print(nam1*nam2)
# print(nam1/nam2)
# print(nam1//nam2)


# # доп
# class Book:
#     def __init__(self, autor, year, name):
#         self.autor = autor
#         self.year = year
#         self.name = name

#     def __str__(self):
#         return f"{self.autor}, {self.year}, {self.name}"

#     def __eq__(self, other):
#         return self.year == other.year
    
#     def __lt__(self, other):
#         return self.year < other.year
    
#     def __le__(self, other):
#         return self.year <= other.year
    
#     def __gt__(self, other):
#         return self.year > other.year
    
#     def __ge__(self, other):
#         return self.year >= other.year
    
#     def __ne__(self, other):
#         return self.year != other.year
    
# book = Book('Пушкин', 1890, 'Залатая рыбка')
# book2 = Book('Толстой', 1800, 'Вайна и мир')
# print(book)
# print(book2)
# print(book==book2)
# print(book<book2)
# print(book<=book2)
# print(book>book2)
# print(book>=book2)   
# print(book!=book2)       
    
    
#Завдання 1
'''Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об’єм двигуна, колір машини,
ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій. '''
#year of manufacture, manufacturer, engine capacity
class Car:
    def __init__(self, modelName, year, manufacturer, engineCapacity, color, price):
        self.modelName = modelName
        self.year = year
        self.manufacturer = manufacturer
        self.engineCapacity = engineCapacity
        self.color = color
        self.price = price
    def set_modelName(self, modelName):
        self.modelName = modelName
    def set_year(self, year):
        self.year = year
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def set_engineCapacity(self, engineCapacity):
        self.engineCapacity = engineCapacity
    def set_color(self, color):
        self.color = color
    def set_price(self, price):
        self.price = price
    def get_modelName(self):
        return self.modelName
    def get_year(self):
        return self.year
    def get_manufacturer(self):
        return self.manufacturer
    def get_engineCapacity(self):
        return self.engineCapacity
    def get_color(self):
        return self.color
    def get_price(self):
        return self.price
    def __str__(self):
        return (f"Model name: {self.modelName}, year of manufacture: {self.year}, manufacturer: {self.manufacturer}, "
              f"engine capacity: {self.engineCapacity}, color: {self.color}, price: {self.price}.")
myCar = Car('honda', 2017, 'yuyt', 150, 'red', 20_000)
print(str(myCar))
print(myCar.price)
myCar.price = 90000
print(myCar.price)
#Завдання 2
'''Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
 Реалізуйте методи класу для введення-виведення даних та інших операцій.'''
class Book:
    def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
    def __str__(self):
        return (f"title: {self.title}, year of publication: {self.year}, publisher: {self.publisher}, "
                f"genre: {self.genre}, author: {self.author}, price:{self.price}.")
    def to_dict(self):
        return {
            "title": self.title,
            "year of publication": self.year,
            "publisher": self.publisher,
            "genre": self.genre,
            "author": self.author,
            "price": self.price
        }
myBook = Book('Франція: історія пригод', 2002, "KСД", "Історія","Г. Робб",334)
print(str(myBook))
print(myBook.to_dict())

#Завдання 3
'''Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
Реалізуйте методи класу для введення-виведення даних та інших операцій.'''
class Stadion:
    def __init__ (self, name, opened_date, country, city, capacity):
        self.name = name
        self.openedDate = opened_date
        self.country = country
        self.city = city
        self.capacity = capacity
    def __bool__(self, c):
        return c <= self.capacity
    def __str__(self):
        return (f'Name: {self.name}, opened Date: {self.openedDate}, country: {self.country}, city: {self.city}, '
                f'capacity: {self.capacity}.')
myStadion = Stadion('arena', '2024-10-09', "Ukraine", "Harkiv", 3000)
print(str(myStadion))
#print(bool(myStadion, 9900))
print(myStadion.__bool__(990))
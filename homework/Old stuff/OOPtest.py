# Задача
# class Person():
#     def __init__(self,_name,_age):
#         self._name = _name
#         self._age = _age

#     def Show_Bio(self):
#         print(self._name)
#         print(self._age)

#     def Change_bio(self,new_name,new_age):
#         self._name = new_name
#         self._age =  new_age

# name1 = Person('Mitko Suhov',33)            
# name1.Change_bio('Ivan Ivanov', 28)
# name1.Show_Bio()
# Задача 
# class Book():
#     def __init__(self,name,autor,year):
#         self.name = name
#         self.autor = autor
#         self.year = year
     
# class Library():
#     def __init__(self):
#         self.books = [['Ujas','Ivan Ivanov',1990],['Fantastica','Georgi Gergiev',200]]
        
#     def Show(self):
#         print(self.books)

#     def Add_book(self,new_book):
#         self.books.append([new_book.name,new_book.autor,new_book.year])


# Libraryy = Library()
# new_book = Book('Roman','Dora Gabe',1975)
# new_book2 = Book('Fatnastika','Totio Totev',1995)
# Libraryy.Add_book(new_book)
# Libraryy.Add_book(new_book2)

# Libraryy.Show()

# Задача

# class Shape():
#     def area(self):
#         pass
           
# class squear(Shape):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def area(self):
#         return self.a*self.b  

# class cur(Shape):
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return self.r*3.14    
        
# tri  = cur(5)      
# sq = squear(4,8)  
        
# print(tri.area())
# print(sq.area())

# Задача 6 
# class Product():
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def Show_product(self):
#         print(self.name) 
#         print(self.price)
#         print(self.quantity)   

# class Inventory():
#     def __init__(self):
        
#         self.products = [['Мляко',1.2,30],['Ябълка',0.75,100]]

#     def Add_product(self,c):
#         self.products.append([c.name,c.price,c.quantity])
#     def Show_product(self):
#         print(self.products)   
# Store = Inventory()
# new = Product('Месо',12,10)         
# Store.Add_product(new)
# Store.Show_product()

# Задача 7 





    

class Laptop:
  def __init__(self,brand,processor,ram,storage):
    self.brand=brand
    self.processor=processor
    self.ram=ram
    self.storage=storage
  def display(self):
    print("Brand:",self.brand)
    print("Processor:",self.processor)
    print("RAM:",self.ram)
    print("Storage:",self.storage)
lap=Laptop("Dell","i5","8GB","1TB")
lap.display()

# output

Brand: Dell
Processor: i5
RAM: 8GB
Storage: 1TB



class Products:
  def __init__(self,id,name,price,quantity):
    self.id=id
    self.name=name
    self.price=price
    self.quantity=quantity
  def display(self):
    print("ID:",self.id)
    print("Name:",self.name)
    print("Price:",self.price)
    print("Quantity:",self.quantity)
products=Products(101,"Pen",10,100)
products.display()

# output

ID: 101
Name: Pen
Price: 10
Quantity: 100



class Movie:
  def __init__(self,title,director,year,language):
    self.title=title
    self.director=director
    self.year=year
    self.language=language
  def display(self):
    print("Title:",self.title)
    print("Director:",self.director)
    print("Year:",self.year)
    print("Language:",self.language)
movie=Movie("Amaran","Rajkumar Periyasamy",2024,"Tamil")
movie.display()

# output

Title: Amaran
Director: Rajkumar Periyasamy
Year: 2024
Language: Tamil



class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def area(self):
    area=self.length*self.width
    print("Length:",self.length)
    print("Width:",self.width)
    print("Area:",area)
rect=Rectangle(10,20)
rect.area()


# output

Length: 10
Width: 20
Area: 200

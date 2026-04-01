# 1. Create a class called Book that has three attributes: length, width, and depth.
# 2. The class should also contain three methods: getVolume(), getWeight(), and setLengthWidthDepth(l, w, d).
# Get methods are used to return the area and weight of the book and set method with three parameters l, w, and d are used to set the state of the objects.
# 3. Finally, create two objects of the Book with different properties initialized as 0.
# 4. Then, update the objects with length, width and depth to 2, 3, 4 for the first object and 9, 8, 7 for the second object.
# 5. Next, call getWidth and getHeight to display the wight and volume of the book objects.
# Note:
# - The volume of the book = length * width * height
# - Weight of a book = 2 * length + 3 * width + 4 * depth



class Book:
    def __init__(self, length = 0, width = 0, depth = 0):
        self.length = length
        self.width = width
        self.depth = depth
    
    def getVolume(self):
        return self.length * self.width * self.depth
    
    def getWeight(self):
        return 2 * self.length + 3 * self.width + 4 * self.depth
    
    def setLengthWidthDepth(self, l, w, d):
        self.length = l
        self.width = w
        self.depth = d
        
    def getArea(self):
        return 2 * (self.length * self.width + self.length * self.depth + self.width * self.depth)
    
first_book = Book(2, 3, 4)

second_book = Book(9, 8, 7)


first_book_width = first_book.getWeight()
second_book_width = second_book.getWeight()

print("First book weight:", first_book_width)
print("Second book weight:", second_book_width)

first_book_volume = first_book.getVolume()
second_book_volume = second_book.getVolume()

print("First book volume:", first_book_volume)
print("Second book volume:", second_book_volume)
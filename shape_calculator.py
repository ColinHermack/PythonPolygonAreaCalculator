class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return(self.width * self.height)
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)
  
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return ("Too big for picture.")
    returnStr = ""
    for i in range(self.height):
      for j in range(self.width):
        returnStr += "*"
      returnStr += "\n"
    return returnStr
  
  def get_amount_inside(self, shape):
    currHeight = 0
    currWidth = 0
    numHeight = 0
    totalNum = 0
    while(currHeight + shape.height <= self.height):
      currHeight += shape.height
      numHeight += 1
    while (currWidth + shape.width <= self.width):
      currWidth += shape.width
      totalNum += numHeight
    
    return totalNum
  
  def __str__(self):
    return("Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")")

  
class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, length):
    self.width = length
    self.height = length

  def set_height(self, length):
    self.width = length
    self.height = length

  def __str__(self):
    return("Square(side=" + str(self.width) + ")")

testRect = Rectangle(4, 8)
testSquare = Square(4)

print(testRect.get_amount_inside(testSquare))
from rectangle import Rectangle

rectangle = Rectangle(5, 3)
print(f"Width: {rectangle.width}, Length: {rectangle.length}, Area: {rectangle.area}")
rectangle.width = 7
print(f"Width: {rectangle.width}, Length: {rectangle.length}, Area: {rectangle.area}")
class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius * 2
        self.__color = str(color)

    def getradius(self):
        return self.__radius

    def getcolor(self):
        return self.__color

    def getarea(self):
        return ((22/7 * (self.getradius()**2)))

    def tostring(self):
        return f"radius: {self.getradius()}" + "\n" + f"color: {self.getcolor()}"

    def setradius(self, newradius):
        self.__radius = newradius * 2

    def setcolor(self, newcolor):
        self.__color = newcolor


class Cylinder(Circle):
    def __init__(self,radius, color, height = 1.0):
        super().__init__(radius, color)
        self.__height = height * 2

    def getheight(self):
        return self.__height

    def setheight(self, newheight):
        self.__height = newheight * 2

    def getvolume(self):
        return ((22/7 * (self.getradius()**2) * self.getheight))
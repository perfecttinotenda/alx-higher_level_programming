#!/usr/bin/python3
"""Rectangle class implement Base class """


from models.base import Base


class Rectangle(Base):
    """ rec_class implement Base _lass
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Returninivate attrte (__width)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setting priv att (__width)
        """
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
            Returning prv attr (___height)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setting pri att(__height)
        """
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """
            Returning priv attr (__x)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setting priv attr (__x)
        """
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
            Returning priv attr (__y)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setting priva attr(__y)
        """
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        """
            Returns tctangle (height * width)
        """
        return (self.height * self.width)

    def display(self):
        """
            Prints to stdo the repreoftangle
        """
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """
            Updates ths prop the class
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns a dictionaryass
        """
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

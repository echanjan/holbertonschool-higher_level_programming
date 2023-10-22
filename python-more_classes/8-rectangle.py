#!/usr/bin/python3
"""
Defines a Rectangle Class
"""


class Rectangle:
    """
    Esta clase define un rectángulo
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Método constructor, recibe el ancho y alto

        Args:
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo
        """
        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Este atributo regresa el ancho del rectángulo

        Returns:
        int: Retorna el ancho(height)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Este atributo configura el ancho del rectángulo.

        Args:
            value (int): Este valor configura el ancho del rectágulo.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Este atributo regresa el alto del rectángulo.

        Returns:
            int: Retorna el alto(height)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Este atributo configura el valor de __height

        Args:
            value (int): Este valor configura el alto del rectángulo.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Este método cálcula el área del rectángulo

        Returns:
            int: alto * ancho
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Este método cálcula el perímetro del rectángulo.
        Sí el ancho o alto es 0, se retornará 0

        Returns:
            int: alto * 2 + ancho * 2
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """
        Este método representa un string de Rectángulo

        Returns:
            str: Regresa un rectángulo con el #.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            a = self.__height + 1
            b = self.__width
            str_repr = ''.join(
                    [f"{str(self.print_symbol) * b}\n" for i in range(a) if i])
            return str_repr[:len(str_repr) - 1]

    def __repr__(self):
        """
        Este método mágico regresa una representación del rectángulo

        Returns:
            string: Cadena que represanta el rectángulo
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Este método imprime un mensaje al eliminar la instancia de Rectangle
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Este método estático compara el árae de 2 rectángulos.
        Ambos deben pertenecer a la misma clase Rectangle.

        Args:
            rect_1 (Rectangle): Instancia de la clase Rectangle
            rect_2 (Rectangle): Instancia de la clase Rectangle

        Raise:
            TypeError : Sí no son instancias de Rectangle.

        Returns:
        rect_1: Retorna la instancia con mayor área.
        """
                                                                                                                        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
                                                                                                                        if not isinstance(rect_2, Rectangle):       
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():                                                                                  return rect_1  
        elif rect_1.area() > rect_2.area():  
            return rect_1
        else:
            return rect_2

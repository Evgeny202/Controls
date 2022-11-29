# Задача 6.

class AirCasyle():
    def __init__(self, height,clouds, color, transparency, n):
        self.height = height
        self.clouds = clouds
        self.color = color
        self.transparency = transparency
        self.n = n

    def change_height(self,value, n):
        self.height = value
        self.clouds += n
        value = value + (n // 5)
        return value

    def visibility(self, height, transparency, clouds):
        visibility = (height // transparency) * clouds
        return visibility

    def __str__(self):
        return f'The AirCastle at an altitude {self.height} meters is {self.color} with {self.clouds} clouds'

    def __gt__(self, other):

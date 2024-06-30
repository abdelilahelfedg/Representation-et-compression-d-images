class Pixel:
    def __init__(self, ValeurR, ValeurG, ValeurB):
        if(0 <= ValeurR <= 255 and 0 <= ValeurG <= 255 and 0 <= ValeurB <= 255):
            self.__ValeurR = ValeurR
            self.__ValeurG = ValeurG
            self.__ValeurB = ValeurB
        else:
            print("les valeurs doivent etre entre 0 et 255")
    def getRouge(self):
        return self.__ValeurR
    def getGreen(self):
        return self.__ValeurG
    def getBlue(self):
        return self.__ValeurB

    def __eq__(self, other):
        if isinstance(other, Pixel):
            return (self.__ValeurR == other.__ValeurR and
                    self.__ValeurG == other.__ValeurG and
                    self.__ValeurB == other.__ValeurB)
        return False

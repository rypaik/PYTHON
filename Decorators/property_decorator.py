

# REGULAR CLASS

# class Temperature:
#   def __init__(self, celcius=0):
#       self._celcius = celcius

#   def get_fahrenheit(self):
#       return (self._celsius * 9 / 5) + 32

# temperature = Temperature(37)

# print(temperature.get_fahrenheit())


# property version 
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    # non - @property getter
    def get_fahrenheit(self):
        return (self._celsius * 9 / 5) + 32
    
    #fahrenhei = property(fget=get_fahrenheit)
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    

temperature = Temperature(37)
print(temperature.fahrenheit)
print(f"Non @property Outuput {temperature.get_fahrenheit()}")





#TODO: AttributeError: 'Temperature_setter' object has no attribute '_celcius'

##  @property SETTER

class Temperature_setter:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('value must be a number')
        self._celsius = (value - 32) * 5 / 9

tempset = Temperature_setter(98)
print(tempset._celcius)
temp.fahrenheit = 98.6 
print(tempset._celcius)

temp = Temperature(36.5)
print(temp)

degrees = int()

#Celsius to fahrenheit
def celsiusToFahrenheit(degrees):
    def to_fahrenheit(degrees):
        return degrees * 1.8 + 32

    result = to_fahrenheit(degrees)
    return result

#Fahrenheit to Celsius
def fahrenheitToCelsius(degrees):
    def to_celsius(degrees):
        return (degrees - 32) / 1.8


    result = to_celsius(degrees)
    return result

#Celsius to Kelvin
def celsiusToKelvin(degrees):
    def to_kelvin(degrees):
        return degrees + 273.15

    result = to_kelvin(degrees)
    return result

#Fahrenheit to Kelvin
def fahrenheitToKelvin(degrees):
    def to_celsius(degrees):
        return (degrees - 32) / 1.8
    cel = to_celsius(degrees)

    def to_kelvin(cel):
        return cel + 273.15
    result = to_kelvin(cel)

    return result

#Kelvin to Celsius
def kelvinToCelsius(degrees):
    def to_celsius(degrees):
        return degrees - 273.15
    result = to_celsius(degrees)
    return result

#Kelvin to Fahrenheit
def kelvinToFahrenheit(degrees):
    def to_celsius(degrees):
        return degrees - 273.15
    cel = to_celsius(degrees)
    def to_fahrenheit(cel):
        return cel * 1.8 + 32

    result = to_fahrenheit(cel)
    return result

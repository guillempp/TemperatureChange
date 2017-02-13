#import declaration.
import TemperatureChange
#input declaration.
degrees = float(input("Degrees? "))
#In this program we are going to convert from Kelvin to Celsius.
#We use a variable called result with the call to the function kelvinToCelsius.
result = TemperatureChange.kelvinToCelsius(degrees)
#Print the result on the screen.
print result, "Celsius"

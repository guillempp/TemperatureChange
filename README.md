#TemperatureChange

[![GitHub version](https://badge.fury.io/gh/guillempp%2FTemperatureChange.svg)](https://badge.fury.io/gh/guillempp%2FTemperatureChange)  ![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)    [![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](github.com/guillempp/TemperatureChange)  [![Twitter Follow](https://img.shields.io/twitter/follow/espadrine.svg?style=social&label=Follow)](twitter.com/guillempp)

This program is intended as an easy way to change temperature units.

##Usage
First you have to make sure the file TemperatureChange.py is in your project folder. It always takes a float and then returns a float.
###Import
Adding the following import statement to your project.
```python
import TemperatureChange
```
###Usage for conversions
####Celsius to Fahrenheit
``` python
TemperatureChange.celsiusToFahrenheit(float)
```
Also can:
``` python
degrees = float(input())
result = TemperatureChange.celsiusToFahrenheit(degrees)
```
#### Fahrenheit to Celsius
``` python
TemperatureChange.fahrenheitToCelsius(float)
```
####Celsius to Kelvin
``` python
TemperatureChange.celsiusToKelvin(float)
```
####Fahrenheit to Kelvin
``` python
TemperatureChange.fahrenheitToKelvin(float)
```
####Kelvin to Celsius
``` python
TemperatureChange.kelvinToCelsius(float)
```
####Kelvin to Fahrenheit
``` python
TemperatureChange.kelvinToFahrenheit(float)
```
### Example.py

``` python
#import declaration.
import TemperatureChange
#input declaration.
degrees = float(input("Degrees? "))
#In this program we are going to convert from Kelvin to Celsius.
#We use a variable called result with the call to the function kelvinToCelsius.
result = TemperatureChange.kelvinToCelsius(degrees)
#Print the result on the screen.
print result, "Celsius"

```

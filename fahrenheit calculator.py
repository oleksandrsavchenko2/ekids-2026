def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32    

def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)   
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

degreesCelsius = float(input("Введіть градуси Цельсія: "))

degreesFahrenheit = convertToFahrenheit(degreesCelsius)

print("Градуси в фаренгейтах:", degreesFahrenheit)

degreesFahrenheit = float(input("Введіть градуси Фаренгейта: "))

degreesCelsius = convertToCelsius(degreesFahrenheit)

print("Градуси в цельсіях:", degreesCelsius)

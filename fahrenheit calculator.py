def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32    

def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)   

degreesCelsius = float(input("Введіть градуси Цельсія: "))

degreesFahrenheit = convertToFahrenheit(degreesCelsius)

print("Градуси в фаренгейтах:", degreesFahrenheit)

degreesFahrenheit = float(input("Введіть градуси Фаренгейта: "))

degreesCelsius = convertToCelsius(degreesFahrenheit)

print("Градуси в цельсіях:", degreesCelsius)
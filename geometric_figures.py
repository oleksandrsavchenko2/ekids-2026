def main():
    from rectangle import perimeter, area

    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26

    print("Прямокутник")

    length = float(input("введіть довжину:"))
    width = float(input("введіть ширину:"))

    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40

    print(f"Площа: {area(length, width)}")

    from parallelepiped import volume, surfaceArea

    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400
    assert surfaceArea(10, 10, 10) == 600
    assert surfaceArea(9999, 0, 9999) == 199960002
    assert surfaceArea(5, 8, 10) == 340

    print("\nПаралелепіпед")

    length = float(input("Введіть довжину:"))
    width = float(input("Введіть ширину:"))
    height = float(input("Введіть висоту:"))

    print(f"Об'єм: {volume(length, width, height)}")
    print(f"Площа поверхні: {surfaceArea(length, width, height)}")
    
main()
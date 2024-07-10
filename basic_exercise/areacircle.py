import math

print(__name__)


def main(radius):
    area = math.pi * radius * radius
    print(f"The area of circle is {round(area,3)}")


if __name__ == "areacircle":
    radius = 0
    radius = float(input("Enter the radius : "))
    main(radius)

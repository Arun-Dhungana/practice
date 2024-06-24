def area(base, height, shape="triangle"):
    if shape == "triangle":
        return 1 / 2 * base * height
    elif shape == "rectangle":
        return base * height
    else:
        print("No valid input shape.")


print(area(10, 20))

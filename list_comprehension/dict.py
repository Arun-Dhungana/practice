integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

zipped = zip(integer, binary)
list = [inte for inte in zipped]
print(list)
dict = {inte: bina for inte, bina in zipped}
print(dict)

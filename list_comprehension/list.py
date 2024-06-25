# Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
# a + i = 0
integer = [1, -1, 2, 3, 5, 0, -7]

list = [-1 * i for i in integer]
print(list)

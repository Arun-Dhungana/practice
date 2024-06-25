def count_up_to(max):
    num = 1
    while num <= max:
        yield num
        num += 1


# Using the generator function
for counter in count_up_to(5):
    print(counter)

for counter in count_up_to(5):
    print(counter)
    print("HI")

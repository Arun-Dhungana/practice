count = {}
with open("poems.txt", "r") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            if word in count:

                count[word] += 1
            else:
                count[word] = 1

max_count = max(count.values())

for w, c in count.items():
    if c == max_count:
        print(f"The max occurence is of word '{w}' with {c} occurences.")

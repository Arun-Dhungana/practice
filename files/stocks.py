with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company name,pe ratio,pb ratio \n")
    next(f)
    for lines in f:
        token = lines.split(",")
        price = int(token[1])
        earnig = int(token[2])
        booking = int(token[3])
        pe = round(float(price / booking), 2)
        pb = round(float(price / booking), 2)
        out.write(f"{token[0]},{pe},{pb}\n")

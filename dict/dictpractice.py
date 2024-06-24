country = {"china": 200, "india": 136, "usa": 32, "pakistan": 21}
import statistics

avg = statistics.mean(country.values())
print(avg)


def print_all():
    for i, popn in country.items():
        print(f"{i.capitalize()}-->{popn}")


def add():
    name = input("Enter the name of country: ")
    name = name.lower()
    if name in country:
        print("Country already in list.Bye!!")
        return
    popn = input("Enter the population: ")
    popn = popn.lower()
    country[name] = popn
    print_all()


def deet():
    name = input("Enter the name of country you want to delete: ")
    name = name.lower()
    if name not in country:
        print("Country not in list.Bye!!")
        return

    del country[name]
    print_all()


def query():
    name = input("Enter the name of country you want to knw about: ")
    name = name.lower()
    if name not in country:
        print("Country not in list.Bye!!")
        return

    print(f"The population of {name.capitalize()} is {country[name]} crores.")


def main():
    func = input("Enter the function you want to perform:(print,add,del,query): ")
    cmd = func.lower()
    if cmd == "print":
        print_all()
    elif cmd == "add":
        add()
    elif cmd == "del":
        deet()
    if cmd == "query":
        query()
    else:
        print("Wrong command!!!!")


if __name__ == "__main__":
    main()

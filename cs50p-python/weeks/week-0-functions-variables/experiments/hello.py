# CS50P Week 0 Experiment: Strings and Functions


def main():
    name = input("Enter name: ").strip().title()
    hello(name)


def hello(to="world"):
    print(f"hello, {to}")


main()


# Previous experiments:
#
# name = input("Enter name: ").strip().title()
# first, last = name.split(" ")
# print(f"Hello, {last}")
#
# def hello(name):
#     print("hello", name)
#
# hello("Rohan")
# hello("David")
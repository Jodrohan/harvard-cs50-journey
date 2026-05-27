# CS50P Week 0 Experiment: Numbers, Formatting, and Functions


def main():
    x = int(input("Enter number: "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)


main()


# Previous experiments:
#
# Addition with integers
#
# a = int(input("What's a? "))
# b = int(input("What's b? "))
# print(a + b)
#
#
# Addition with floats and comma formatting
#
# a = float(input("What's a? "))
# b = float(input("What's b? "))
# z = a + b
# print(f"{z:,}")
#
#
# Division with round()
#
# a = float(input("What's a? "))
# b = float(input("What's b? "))
# z = a / b
# print(round(z, 2))
#
#
# Division with f-string decimal formatting
#
# a = float(input("What's a? "))
# b = float(input("What's b? "))
# z = a / b
# print(f"{z:.2f}")
"""


Prompts the user for a fractional fuel level (X/Y), calculates the 
corresponding percentage, and outputs the appropriate gauge reading.
"""
def main():
    while True:
        try:
            user_input = input("What's x/y? ")
            number = convert(user_input)
            final_result = gauge(number)
            print(final_result)           
            break
            
        except (ValueError, ZeroDivisionError):
            pass
def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    percentage = (x/y)*100
    return round(percentage)

def gauge(percentage):

    if percentage <=1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
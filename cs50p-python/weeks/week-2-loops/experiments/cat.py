def main():
    """Main execution function to get a number and print meows."""
    number = get_number()
    meow(number)

def get_number():
    """Prompts the user for a positive integer, validating the input."""
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
            
def meow(n):
    """Prints 'meow' n times using a throwaway variable."""
    for _ in range(n):
        print("meow")


main()
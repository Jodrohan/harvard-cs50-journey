def main():
    """Main execution block."""
    print_square(3)

def print_square(size):
    """Prints a square of # blocks using an abstracted row function."""
    for i in range(size):
       print_row(size)

def print_row(width):
    """Prints a single row of # blocks."""
    print("#" * width)

# Trigger the program
main()
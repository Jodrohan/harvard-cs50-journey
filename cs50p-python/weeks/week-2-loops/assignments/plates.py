"""
Vanity Plates

In Massachusetts, home to some of the most vanity plates in the world, 
vehicles can be equipped with vanity plates with your personalized choices of 
letters and numbers. All vanity plates must comply with the following 
requirements:

1. “All vanity plates must start with at least two letters.”
2. “Vanity plates may contain a maximum of 6 characters (2–6 characters) 
   and a minimum of 2 characters.”
3. “Numbers cannot be used in the middle of a plate; they must come at 
   the end. For example, AAA222 would be an acceptable vanity plate; 
   AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
4. “No periods, spaces, or punctuation marks are allowed.”

Implement a program that prompts the user for a vanity plate and then 
outputs “Valid” if it meets all of the requirements or “Invalid” if it 
does not. Assume that any alphanumeric characters (A-Z and 0-9) are 
legal.
"""
def main():
    plate = input("Enter Number: ")
    if vanity_checker(plate):
        print("Valid")
    else:
        print("Invalid")


def vanity_checker(vanity):

    if not vanity[0:2].isalpha():
        return False
    if not 2 <= len(vanity) <= 6:
        return False
    number_started = False
    for char in vanity:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif char.isalpha():
            if number_started:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    main()



  

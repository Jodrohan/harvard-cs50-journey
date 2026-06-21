'''
Testing Vanity Plates


'''
def main():
    plate = input("Enter the vanity numer: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")
def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    p = s[0:2]
    if not p.isalpha():
        return False
    number_started = False
    for char in s:
        if char.isdigit():
                if not number_started:
                    if char == "0":
                        return False
                    else:
                        number_started = True
        elif char.isalpha():
            if number_started:
                return False
        else:
            return False
    return True
if __name__ == "__main__":
    main()
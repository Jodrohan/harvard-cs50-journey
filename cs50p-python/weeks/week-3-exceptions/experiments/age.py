def main():
    while True:
        try:
            age = int(input("What's age? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            break
    print(f"Age logged: {age}")

if __name__ == "__main__":
    main()
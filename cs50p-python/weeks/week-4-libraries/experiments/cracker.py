import sys
import hashlib
def main():
    try:
        print("Argument", sys.argv[1])
        target_hash = sys.argv[1]
    except IndexError:
        print("Where is the input? ")

        sys.exit()
    else:
        rockyou_mock = [
            "admin123",
            "123456",
            "qwerty",
            "shadow",
            "password",
            "hunter2",
            "letmein",
            "Leerohan@1"
        ]
        for password in rockyou_mock:
            hashed_guess = hashlib.sha256(password.encode()).hexdigest()
            if hashed_guess == target_hash:
                print(f"Password cracked {password}")
                break
            
        else:
            print("Password not found in dictionary.")


if __name__ == "__main__":
    main()

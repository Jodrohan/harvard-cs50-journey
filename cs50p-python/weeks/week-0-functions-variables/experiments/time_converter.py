# Ask the user to input a time (like 2:15), use a custom function to calculate the total minutes, and print the result.

def main():
    time_str = input("Enter a time (like 02:15) : ")
    hour, minutes = time_str.split(":")
    hour = hour_to_minutes(int(hour))
    minutes = int(minutes)
    print(f"total_minutes = {hour + minutes}")

def hour_to_minutes(h):
    h = h*60
    return h

main()
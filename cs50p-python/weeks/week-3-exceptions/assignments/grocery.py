"""
Grocery List
This program prompts the user for items, one per line, until the user
inputs control-d (which is a common way of ending one's input to a program).
Then it outputs the user's grocery list in all uppercase, sorted
alphabetically by item, prefixing each line with the number of times
the user inputted that item.
"""
def main():
    grocery_list = {}
    while True:
        try:
            items = input().upper().strip()
        except EOFError:
            print()
            break
            
            
        else:
            if items in grocery_list:
                grocery_list[items]+=1
            else:
                grocery_list[items] = 1
    for items in sorted(grocery_list.keys()):
        print(f"{grocery_list[items]} {items}")


if __name__ == "__main__":
    main()
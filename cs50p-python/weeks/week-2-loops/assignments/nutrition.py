"""
In a file called nutrition.py, implement a program that prompts consumers users to 
input a fruit (case-insensitively) and then outputs the number of calories in one 
portion of that fruit, per the FDA’s poster for fruits, which is available at 
https://www.fda.gov/media/68379/download. 

Capitalization aside, assume that users will input fruits exactly as written in 
the poster (e.g., "Strawberries", not "strawberry"). 

- If the user’s input is not a fruit, do not output anything.
- Your program should be case-insensitive.
"""


def main():
    fruits = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80,
    }
    fruit = input("Item: ").strip().lower()
    if fruit in fruits:
        print(fruits[fruit])
    

main()
#Write a Python program that replaces :) with 🙂 and :( with 🙁 in user input.

def main():
    emoji = convert(input())
    print(emoji)
def convert(c):
    c = c.replace(":)","🙂")
    c = c.replace(":(","🙁")
    return c
main()
#Write a Python program that replaces :) with 🙂 and :( with 🙁 in user input.

emoji = input("Enter the string: ")


emoji=emoji.replace(":)","🙂")
emoji=emoji.replace(":(","🙁")
print(emoji)
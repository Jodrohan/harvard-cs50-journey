'''
Just setting up my twttr

When texting or tweeting, it’s not uncommon to shorten words to save time or space, 
for instance by omitting vowels.

Implement a program that prompts the user for a str of text and then outputs 
that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted 
in uppercase or lowercase.

For Week 5 requirements, restructure your code so that it includes a function 
called `shorten` that expects a str as input and returns that same str but 
with all vowels omitted.
'''



def main():
    user_input = input("What's text? ")
    omitted_string = shorten(user_input)
    print(f"Omitted string: {omitted_string}")
                


def shorten(word):
    vowels = ("aeiouAEIOU")
    omitted_string = word
    for vowel in vowels:
        if vowel in word:
            omitted_string = omitted_string.replace(vowel,"")
    return omitted_string
    

if __name__ == "__main__":
    main()

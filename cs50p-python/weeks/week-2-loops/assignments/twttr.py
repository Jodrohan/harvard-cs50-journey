'''Twitter, now known as X, is an online social media and social networking service where users post 
   and interact with messages called “tweets,” traditionally restricted to 140 characters.

Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U)
omitted, whether inputted in uppercase or lowercase.

Requirements:

    You should output the text exactly as the user typed it, just with the vowels removed.

    Preserve case (e.g., if the user types "Hello", you should output "Hll").

    Assume that any of the letters A, E, I, O, or U (in either case) are vowels.

    Do not remove other characters (like spaces, punctuation, or numbers).'''


def main():
   text = omitted(input("Enter text: "))
   print(text)
def omitted(text):
    result = ""
    vowels = "AEIOUaeiou"
    for char in text:
        if char not in vowels:
           result+=char
    return result
if __name__ =="__main__":
    main()


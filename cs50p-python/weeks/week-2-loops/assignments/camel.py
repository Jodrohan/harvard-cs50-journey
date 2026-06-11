"""
camelCase

In a file called camel.py, implement a program that prompts the user for 
the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user's input will indeed be in camel case.
"""

'''def main():
    camel_case = snake_case(input("Enter the text: "))
    
    print(camel_case)



def snake_case(s):
    result = ("")
    for char in s:
        
        if char.isupper():
            result +="_" + char.lower()
        else:
            result += char


    return result



main()
'''

def main():
    camel_case = snake_case(input("Enter the text: "))
    print(camel_case)

def snake_case(s):
    result=("")
    for char in s:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result

main()

            



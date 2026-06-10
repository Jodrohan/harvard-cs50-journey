"""
camelCase

In a file called camel.py, implement a program that prompts the user for 
the name of a variable in camel case and outputs the corresponding name in snake case. 
Assume that the user's input will indeed be in camel case.
"""


def main():
    # Get user input
    camel_input = input("camelCase: ")
    
    
    snake_output = convert_to_snake(camel_input)
    
    
    print(f"snake_case: {snake_output}")

def convert_to_snake(camel_str):
    
    snake_result = ""
    
    
    for char in camel_str:
        
        if char.isupper():
            
            snake_result += "_" + char.lower()
        else:
            
            snake_result += char
            
    return snake_result


if __name__ == "__main__":
    main()
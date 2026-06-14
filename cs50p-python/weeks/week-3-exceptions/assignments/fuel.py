'''
Fuel Gauge (fuel.py)

Implement a program that prompts the user for a fraction, formatted as X/Y, 
wherein each of X and Y is an integer, and then outputs, as a percentage rounded 
to the nearest integer, how much fuel is in the tank. 

Requirements:
- If 1% or less remains, output E instead to indicate that the tank is essentially empty.
- If 99% or more remains, output F instead to indicate that the tank is essentially full.
- If X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
- You must handle ValueError and ZeroDivisionError gracefully.
'''

def main():
    while True:
        try:
            fraction = input("Provide Fraction (x/y)? ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            percentage = (x/y)*100
            rounded = round(percentage)
            
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if rounded <= 1:
                print("E")
            elif rounded >=99:
                print("F")
            else:
                print(f"{rounded}%")
            break
if __name__ == "__main__":
    main()

            
            
            


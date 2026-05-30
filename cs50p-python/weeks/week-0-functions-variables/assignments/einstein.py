#Write a Python program that asks the user for mass as an integer and calculates energy using Einstein’s formula:
#E = m × c²
#where c = 300000000

def main():
    m = int(input("m: "))
    c = 300000000
    E = m*c*c
    print(E)

main()

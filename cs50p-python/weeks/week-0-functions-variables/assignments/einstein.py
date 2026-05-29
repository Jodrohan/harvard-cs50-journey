#Write a Python program that asks the user for mass as an integer and calculates energy using Einstein’s formula:

#E = m × c²

#where c = 300000000


mass = int(input("Enter mass: "))
c = 300000000
E = mass*c*c
print(E)

"""
CS50P Week 8, Assignment 2: Cookie Jar

Implement a class called Jar in a file called jar.py with the following methods and properties:

- __init__(self, capacity=12): Initializes a cookie jar with the given capacity. 
  If capacity is not a non-negative int, raise a ValueError.
  
- __str__(self): Returns a string with n 🍪 emojis, where n is the number of cookies currently in the jar.

- deposit(self, n): Adds n cookies to the cookie jar. 
  If adding that many would exceed the cookie jar's capacity, raise a ValueError.
  
- withdraw(self, n): Removes n cookies from the cookie jar. 
  If there aren't that many cookies in the cookie jar, raise a ValueError.
  
- @property capacity: Returns the cookie jar's capacity.

- @property size: Returns the number of cookies actually in the cookie jar.
"""
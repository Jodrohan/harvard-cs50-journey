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

class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
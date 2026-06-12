"""
Coke Machine

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents each and 
only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

Implement a program that prompts the user to insert a coin, one at a time, 
each time prompting the user "Insert Coin:". 

1. You should always output how much money is still owed to the machine 
   (start at 50 cents).
2. If the user inserts a coin that is not 25, 10, or 5 cents, ignore it 
   and keep showing the amount due.
3. Once the user has inserted at least 50 cents, stop the loop and output 
   how many cents in change the user is owed (e.g., "Change Owed: 10").
"""


def main():
   amount_due = 50
   while amount_due > 0:
      print(f"Amount Due: {amount_due}")
      coin = int(input("Insert coin: "))
      if coin in [5, 10, 25]:
         amount_due -= coin

   print(f"Change Owed: {-amount_due}")

if "__name__" == "__main__":
   main()


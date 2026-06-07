"""
Problem Set 5: Meal Time (meal.py)

The Goal:
Prompt the user for a time and tell them which meal they should be eating based on that time.

The Rules:
1. Prompt the user for a time in 24-hour format (e.g., "7:30" or "18:00").
2. Write a specific function called `convert(time)` that takes that string ("7:30") and converts it into a decimal float (7.5).
3. Using the float returned by `convert`, output:
   - "breakfast time" (if between 7:00 and 8:00)
   - "lunch time" (if between 12:00 and 13:00)
   - "dinner time" (if between 18:00 and 19:00)
4. If it is not time for any of those meals, output nothing at all.
"""
def main():

   time = convert(input("Time: "))
   if 7.0 <= time <=8.0:
      print("breakfast time")
   elif 12.0 <= time <= 13.0:
      print("lunch time")
   elif 18.0 <= time <= 19.0:
      print("dinner time")
   

def convert(t):

   hour, minute = t.split(":")
   hour = int(hour)
   minute = int(minute)
   minute = (minute/60)
   t = hour + minute
   return t

if __name__ == "__main__":
   main()


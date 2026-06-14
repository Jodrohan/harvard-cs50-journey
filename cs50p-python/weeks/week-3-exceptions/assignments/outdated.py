"""
Outdated
This program prompts the user for a date, in month-day-year order, formatted
like 9/8/1636 or September 8, 1636. Then it outputs that same date in 
YYYY-MM-DD format.

Requirements:
1. If the user's input is not a valid date in either format, prompt again.
2. The month must be 1–12 and the day must be 1–31.
3. Handle both numeric dates (9/8/1636) and written dates (September 8, 1636).
4. Output must be in YYYY-MM-DD format, with months and days padded 
   with zeros if necessary (e.g., 09-08).
"""
def main():
    months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"]
    while True:
        date = input("Enter date: ").strip()
        
        try:
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                date = date.replace(",","")
                month, day, year = date.split(" ")
                
                month = months.index(month)+1
            else:
                continue

            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <=day<= 31 and 1 <=month<= 12:
                print(f"{year}-{month:02d}-{day:02d}")
                break
            
        except (ValueError, IndexError):
            pass
        

if __name__ == "__main__":
    main()

                


            

         
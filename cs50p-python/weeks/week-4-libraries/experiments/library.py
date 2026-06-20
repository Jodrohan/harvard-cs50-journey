"""
PROBLEM BRIEF: Secure Library Manager
-------------------------------------
Your task is to develop a robust command-line utility that processes a library's 
inventory log. The system must ingest a text file containing formatted book 
records, transform that data into a structured format, and perform a status 
aggregation.

INPUT:
    A filename provided via command-line arguments (sys.argv).
    Format of the file: Each line represents one book in the following format:
    "title:BookTitle,author:AuthorName,status:available"
    (where status is either "available" or "checked_out")

FUNCTIONAL REQUIREMENTS:
    1. Input Validation: Verify the user provided a filename. 
       Handle missing arguments gracefully.
    2. Fault Tolerance: Implement `try...except` blocks to handle:
       - FileNotFoundError (if the file doesn't exist).
       - Permission errors or malformed lines.
    3. Data Transformation: Convert raw string records into a list of 
       dictionaries for easy indexing.
    4. Business Logic: Aggregate the library state by counting occurrences of 
       'checked_out' vs 'available' books across the entire inventory.
    5. Output: Display the final counts clearly to the user.

DESIGN CONSTRAINTS:
    - Code must be modularized using a `main()` function.
    - Execution must be protected by the `if __name__ == "__main__":` guard.
    - No external libraries (only standard libraries like sys, os, etc.).
"""
"""
Library Inventory Manager
Parses raw text data into structured dictionaries and calculates inventory statistics.
"""

def main():

    
   raw_library_data = [
        "title:The Great Gatsby,author:F. Scott Fitzgerald,status:available",
        "title:1984,author:George Orwell,status:checked_out",
        "title:The Hobbit,author:J.R.R. Tolkien,status:available",
        "title:Fahrenheit 451,author:Ray Bradbury,status:checked_out",
        "title:The Catcher in the Rye,author:J.D. Salinger,status:available"
   ]
   
    
   books = []
   for entry in raw_library_data:
        book_dict = {}
        for pair in entry.split(","):
            key, value = pair.split(":")
            book_dict[key] = value
        books.append(book_dict)

   final_avail, final_checked = calculate_inventory_stats(books)
   print(f"Available_Count: {final_avail}")
   print(f"Checked Count: {final_checked}")



def calculate_inventory_stats(books):
   available_count = 0
   checked_out_count = 0
   for book in books:
      if book["status"] == "available":
         available_count += 1

      elif book["status"] == "checked_out":
         checked_out_count += 1
   return available_count, checked_out_count

if __name__ == "__main__":
   main()
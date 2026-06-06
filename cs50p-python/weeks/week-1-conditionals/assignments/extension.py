"""
Problem Set 3: File Extensions (extensions.py)

The Goal:
Prompt the user for a file name and output that file's "media type" (also known as a MIME type).

The Rules:
1. Prompt the user for a file name.
2. Ignore leading/trailing whitespace and treat it case-insensitively.
3. If the file ends in:
   - .gif  -> output: image/gif
   - .jpg  -> output: image/jpeg
   - .jpeg -> output: image/jpeg
   - .png  -> output: image/png
   - .pdf  -> output: application/pdf
   - .txt  -> output: text/plain
   - .zip  -> output: application/zip
4. If it ends in anything else (or has no extension), output: application/octet-stream
"""
file_name = input("File name: ").strip().lower()

if file_name.endswith(".gif"):
   print("image/gif")
elif file_name.endswith(".jpg"):
   print("image/jpeg")
elif file_name.endswith(".jpeg"):
   print("image/jpeg")
elif file_name.endswith(".png"):
   print("image/png")
elif file_name.endswith(".pdf"):
   print("application/pdf")
elif file_name.endswith(".txt"):
   print("text/plain")
elif file_name.endswith(".zip"):
   print("application/zip")

else:
   print("application/octet-stream")
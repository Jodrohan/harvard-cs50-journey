"""
Assignment 2: Watch on YouTube

Objective:
Implement a function called `parse` that extracts the YouTube video link from an HTML <iframe> tag 
and converts it to a shorter, shareable youtu.be URL.

Requirements:
1. Define a function `parse(s)` that expects a string of HTML as input.
2. Use the `re` module to search the string for an <iframe> tag containing a 'src' attribute 
   that links to a YouTube video.
3. The YouTube URL embedded within the 'src' attribute might be formatted in several ways:
   - http://youtube.com/embed/[VIDEO_ID]
   - https://youtube.com/embed/[VIDEO_ID]
   - https://www.youtube.com/embed/[VIDEO_ID]
4. If a valid YouTube URL is found, extract the video ID and return a shortened URL 
   in the exact format: https://youtu.be/[VIDEO_ID]
5. If the input does not contain a valid YouTube <iframe> tag, return None.
6. Your program must contain a `main` function that prompts the user for HTML, 
   calls `parse`, and prints the result.

Example Usage:
Input:  <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
Output: https://youtu.be/xvFZjo5PgG0
"""

import re
import sys


def main():
    try:
        url = input("HTML: ").strip()
    except EOFError:
        sys.exit("Program Stopped")
        
    print(parse(url))


def parse(s):
    search = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s)
    
    if search:
        video_id = search.group(1)
        return f"https://youtu.be/{video_id}"
        
    return None


if __name__ == "__main__":
    main()

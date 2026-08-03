"""
Design an object-oriented 'CoursePortal' class to manage IIT Madras BS Degree assignment deadlines.

Requirements:
1. Initialization: 
   The class should take 'course_name' and 'student_id' upon instantiation. 
   It must also internally initialize an empty list attribute called 'assignments'.

2. add_assignment(self, task_name, days_until_due):
   Appends a dictionary (e.g., {"task": task_name, "due_in": days_until_due}) to the 
   assignments list. If 'days_until_due' is less than 0, raise a ValueError with 
   the message "Deadline cannot be in the past".

3. String Representation (__str__):
   When the object is printed, it should return a string in this exact format:
   "Portal for [student_id] - [course_name]: [X] pending assignments" 
   (where [X] is the current total number of assignments in the list).

4. Class Method (from_string):
   Implement a @classmethod that instantiates a CoursePortal from a single string 
   formatted as "CourseName-StudentID" (e.g., "Programming in Python-26f1000001"). 
   It should split the string at the hyphen and return a new instance of the class.
"""
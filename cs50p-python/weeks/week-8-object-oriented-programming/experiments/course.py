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
class CoursePortal:
    def __init__(self, course_name, student_id):
        self.course_name = course_name
        self.student_id = student_id
        self.assignments = []

    def add_assignment(self, task_name, days_until_due):
        if days_until_due < 0:
            raise ValueError("Deadline cannot be in the past")
        
        # Appends the dictionary to our internal list
        self.assignments.append({"task": task_name, "due_in": days_until_due})

    def __str__(self):
        # Uses len() to dynamically get the number of pending assignments
        return f"Portal for {self.student_id} - {self.course_name}: {len(self.assignments)} pending assignments"

    @classmethod
    def from_string(cls, data_string):
        # Splits the string into two variables at the hyphen
        course_name, student_id = data_string.split("-")
        
        # Instantiates and returns a new object of the class
        return cls(course_name, student_id)


def main():
    # 1. Test standard initialization
    portal1 = CoursePortal("Data Science", "26f123456")
    
    # 2. Test adding valid assignments
    portal1.add_assignment("Week 1 Graded", 3)
    portal1.add_assignment("Week 2 Practice", 10)
    
    # 3. Test the __str__ method (automatically called by print)
    print(portal1) 
    
    # 4. Test the @classmethod
    portal2 = CoursePortal.from_string("Programming in Python-26f987654")
    print(portal2)
    
    # 5. Uncommenting the line below will test the ValueError
    # portal1.add_assignment("Late Submission", -2) 

if __name__ == "__main__":
    main()
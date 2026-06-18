'''
Gradebook Aggregator
1. You have a dictionary representing a school system.
2. The structure:
   - A list of classes.
   - Each class has a list of students.
   - Each student has a list of their grades.
3. Your goal: Calculate the class average for every class, 
   and then print the overall average of the entire school.

Pseudo-code:
    - DEFINE data structure (nested lists/dictionaries)
    - INITIALIZE total_school_sum = 0
    - INITIALIZE total_school_count = 0
    - FOR each class IN school:
        - INITIALIZE class_sum = 0
        - INITIALIZE class_count = 0
        - FOR each student IN class['students']:
            - FOR each grade IN student['grades']:
                - ADD grade TO class_sum
                - ADD grade TO total_school_sum
                - INCREMENT counts
        - CALCULATE class_average
        - PRINT class_average
    - CALCULATE and PRINT total_school_average
'''

def main():
    total_school_sum = 0
    total_school_count = 0
    school = [
        {
            "class_name" : "mathematics",
            "students" : [
                {"name": "Alice", "grades":[85,90,92]},
                {"name": "Bob", "grades": [78,81,85]}
            ]
            
        },

        {
            "class_name": "History",
            "students": [
                {"name": "Charlie", "grades": [90, 95]},
                {"name": "David", "grades": [88, 82, 85]}
            ]
        }
            ]
    
        
    for each_class in school:
        class_sum = 0
        class_count = 0
        for each_student in each_class["students"]:
            for each_grade in each_student["grades"]:
                class_sum += each_grade
                total_school_sum += each_grade
                class_count += 1
                total_school_count += 1
            
        class_average = class_sum/class_count
        total_school_average = total_school_sum/total_school_count
        print(f"Average for {each_class['class_name']}: {class_average:.2f}")
    print(f"Total School Average: {total_school_average:.2f}")
    
if __name__ == "__main__":
    main()





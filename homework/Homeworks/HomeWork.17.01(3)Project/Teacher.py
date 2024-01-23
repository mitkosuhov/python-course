from person import Person
from employee import Employee

class Teacher(Person,Employee):
    def teach():
        return "teaching..."
    

print(Teacher.get_fired())
print(Teacher.teach())
print(Teacher.sleep())
    
    
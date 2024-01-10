class Subject():
    def _init_(self , name , gradess):
        self.name = name 
        self.gradess = gradess

    def add_grade(self,grade):
        self.__grades.append(grade)        
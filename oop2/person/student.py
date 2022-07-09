from person import Preson
class Student(Preson):
    def __init__(self,name,faculty,major,year) -> None:
        super().__init__(name)
        self.faculty = faculty
        self.major = major
        self.year = year   
        
    def welcome(self):
        super().welcome()
        print(f'Welcome to {self.faculty} major {self.major} in {self.year}')
        
    

   
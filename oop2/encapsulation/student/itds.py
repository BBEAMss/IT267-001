from student import Student

class ITDS(Student):
    def __init__(self, stuid, name, major) -> None:
        super().__init__(stuid, name, major)

    def _displayNameAndMajor(self):
        print(f'ITDS Name: {self.name}')
        super()._displayNameAndMajor()

stu = ITDS("640108","Amorn", "Information Technology")
stu._displayNameAndMajor()
        
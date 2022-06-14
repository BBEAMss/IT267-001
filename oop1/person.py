class person:
    country = "Thaniland" #class variable
    def __init__(self,name,gender,profession,hours) -> None:
        #instance variables
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours

    def work(self):
        print(f"{self.name} is working as a {self.profession}")

    def study(self):
        print(f"{self.name} studies for {self.hours}hour(s)")

    def show(self):
        print(f"Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.hours}")

    def __del__(self):
        print(f'Object Destroyed')

#create object
jessa = person("Jessa","Male","Software Engineer","10")
jessa.show()
jessa.work()
jessa.study()

jon = person("Jon","Male","Doctor","15")
jon.show()
jon.work()
jon.study()

lalisa = person("Lalisa","Female","Korean Singer","13")
lalisa.work()

print(f"Class variable: {person.country}")
print(f"Instance Variable: {lalisa.country}")

#assing value
lalisa.country = "Korea"
print("------")
print(f"Class variable: {person.country}")
print(f"Instance Variable: {lalisa.country}")
print(f"Instance Variable: {jon.country}")

#assing calss varible
person.country = "England"
print("*******")
print(f"Class variable: {person.country}")
print(f"Instance Variable: {lalisa.country}")
print(f"Instance Variable: {jon.country}")
class Student:
    def __init__(self,name,notes):
        self.name=name
        self.notes=notes
    def average(self):
        return (self.notes[0]+self.notes[1]+self.notes[2])/3
    def printinformations(self):
        return f' the average of {self.name} is {self.average():.2f}'

student1=Student("mina",[19,13,16])
student2=Student("david",[6,17,12])
student3=Student("john",[16,8,20])

print(student1.printinformations())
print(student2.printinformations())
print(student3.printinformations())


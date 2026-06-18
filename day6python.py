import csv
while True:
       choice=int(input("""  enter your choice:  
       1.Add a student.
       2.Display all students.
       3.search about student notes.
       4.exit.                    """))
       if 1<=choice<=4:
           if choice==1:
               name=input("enter your name ")
               note1=int(input("enter note1 "))
               note2=int(input("enter note2 "))
               note3=int(input("enter note3 "))
               with open("day6python.csv","a", newline="") as file:
                   writer=csv.DictWriter(file,fieldnames=["name","note1","note2","note3"])
                   writer.writerow({"name":name,"note1":note1,"note2":note2,"note3":note3})
           elif choice==2:
               with open("day6python.csv", "r") as f:
                   reader = csv.DictReader(f)
                   students = list(reader)
                   for row in sorted(students,key=lambda row: (int(row['note1']) + int(row['note2']) + int(row['note3'])) / 3, reverse=True):
                       print(f"name:{row['name']},note1: {row['note1']},note2: {row['note2']},note3: {row['note3']}")
           elif choice==3:
               with open("day6python.csv", "r") as f:
                   reader = csv.DictReader(f)
                   students = list(reader)
                   search = input("enter name: ")
                   for row in students:
                       if row['name'] == search:
                           print(f"note1: {row['note1']},note2: {row['note2']},note3: {row['note3']}")
           else:
               break
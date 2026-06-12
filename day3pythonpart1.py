def main():   
    tasks=[]
    completedTask=0
    while True:
        choicenum=choice()
        match choicenum:
            case 1:
                AddTask(tasks)
            case 2:
                displayTasks(tasks)
            case 3:
                print(markCompletedTask(tasks))
                completedTask+=1
            case 4:
                displaySummary(completedTask,tasks)
            case 5:
                break
   

def choice():
    while True:
       choice=int(input("""  enter your choice:  
       1.Add a task.
       2.Display all tasks.
       3.Mark a task as completed.
       4.Display a summary at the end showing how many tasks are completed and how many are remaining.
       5.exit                     """))
       if 1<=choice<=5:
           return choice
       
def AddTask(mytasks):
    task=input("enter the new task ")
    mytasks.append(task)

def displayTasks(mytasks):
    i=1
    for task in mytasks:
        print(i,task,sep=".")
        i+=1

def markCompletedTask(mytasks):
    displayTasks(mytasks)
    while True:
        choice=int(input("enter the index of the completed task "))
        if choice >=1 and choice<len(mytasks):
            break
    complete=mytasks[choice]
    mytasks.pop(choice - 1) 
    return complete

def displaySummary(complete,mytasks):
    print(f"""completed tasks={complete}
Remaining tasks={len(mytasks)}""")
    
main()
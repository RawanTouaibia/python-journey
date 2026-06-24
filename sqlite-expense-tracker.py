def main():  
    import sqlite3

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount REAL,
        date TEXT  )
    """)
    conn.commit() 
    while True:
        choicenum=choice()
        match choicenum:
            case 1:
                AddExpense(cursor,conn)
            case 2:
                ViewAllExpenses(cursor)
            case 3:
                s=ViewTotalExpenses(cursor)
                print(f"the total expenses is {s}DA")
            case 4:
                DeleteExpense(cursor,conn)
            case 5:
                conn.close()
                break
   

def choice():
    while True:
       choice=int(input("""  enter your choice:  
       1.Add an Expense
       2.View All Expenses
       3.View Total Expenses
       4.Delete an Expense by its Number
       5.exit                     """))
       if 1<=choice<=5:
           return choice
def AddExpense(c,co):
    name=input("enter the expense name ")
    amount=int(input("enter the amount "))
    date=input("enter the date ")
    with co:
        c.execute("INSERT INTO expenses (name, amount, date) VALUES(:name,:amount,:date)",{'name':name ,'amount':amount ,'date':date})
    co.commit()
def ViewAllExpenses(c):
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    for row in rows:
        print(row)
def ViewTotalExpenses(c):
    sum=0
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    for row in rows:
        sum+=row[2]
    return sum
def DeleteExpense(c,co):
    id=int(input("enter the id of the expense that you want to delete it "))
    with co:
        c.execute("DELETE from expenses WHERE id = :id",{'id':id,})
    co.commit()

main()



    
       

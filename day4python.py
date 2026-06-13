def main():
    while True:
        x=get_int("what's x  ")
        y=get_int("what's y  ")
        operation=get_operation("enter the operation  ")
        match operation:
            case '+':
                print(f"{x}+{y}= {x+y}")
            case '-':
                print(f"{x}-{y}= {x-y}")
            case '*':
                print(f"{x}*{y}= {x*y}")
            case '/':
                try:
                    print(f"{x}/{y}= {x/y}")
                except ZeroDivisionError:
                    print("cannot divide by zero")
            case '%':
                print(f"{x}mod{y}= {x%y}")
        z=YesOrNo("Do you want another calculation? ")
        if z=='n' or z=='N':
            break

def get_int(prompt):
    while True:
        try:
            x=int(input(prompt))
            return x
        except ValueError:
            pass

def get_operation(prompt):
    while True:
        try:
            op = input(prompt)
            if op not in ['+', '-', '*', '/', '%']:
                raise ValueError
            return op
        except ValueError:
            pass

def YesOrNo(prompt):
    while True:
        try:
            yn = input(prompt)
            if yn not in ['Y', 'y', 'N', 'n']:
                raise ValueError
            return yn
        except ValueError:
            print("enter y or n")
main()
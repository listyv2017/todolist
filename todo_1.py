#module
import sys
import datetime

#help functin
def help():
    #使用方法のテキスト表示
    usage = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    
    print(usage)

#Add a new todo
def add(*a):

    f = open('todo.txt', 'a')
    f.writelines(' '.join(a))
    f.write('\n')
    f.close()

    print(f"Add to list : {' '.join(a)}")

#show remaining task
def ls():

    try:
        nec()

        for i in d:
            print(f"[{i}] : {d[i]}\n")

    except Exception as e:
        print("error in ls")

# delete a task
def del_todo(num):

    try: 

        nec()
        num = int(num)

        with open('todo.txt', 'r+') as f:
        
            lines = f.readlines()
            f.seek(0)
            

            for i in lines:
                if i.strip('\n') != d[num]:
                    f.write(i)
                    print("a")
            f.truncate()

            print(f"[{num}] : {d[num]} is deleted")

    except Exception as e:
        
        print(f"Error: todo #{num} does not exist. Nothing deleted.")

# complete a task
def comp(num):
    try: 

        nec()
        num = int(num)

        with open('todo.txt', 'r+') as f:
        
            lines = f.readlines()
            f.seek(0)

            for i in lines:
                if i.strip('\n') != d[num]:
                    f.write(i)
            f.truncate()

            print(f"[{num}] : {d[num]} is done")

    except Exception as e:
        
        print(f"Error: todo #{num} does not exist. Nothing deleted.")


def nec():

    try:
        f = open("todo.txt", 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c : line})
            c = c+1
        
    except:
        print("error in nec")

if __name__ == '__main__':
        
    
    d = {}
    args = sys.argv
    if args[1] == "del":
        args[1] = "del_todo"
    if args[1] == "complete":
        args[1] = "comp"

    if args[1] == "add" and len(args[2:]) == 0:
        print("Error: Missing todo string. Nothing added!")
    elif args[1] == "del_todo" and len(args[2:]) == 0:
        print("Error: Missing NUMBER for deleting todo.")
    elif args[1] == "ls":
        eval(args[1])()
    else:
        eval(args[1])(*args[2:])

    

commands=["add","liste","mark","archive"]
todolist=[]
marklist=[]
marked="[x]"
notmarked="[]"

def add():
       a=input("Add an item: ")
       todolist.append(a)
       marklist.append(notmarked)
       print("Item added.")

def liste():
       print("You saved the following to-do items:")
       for i in range(0,len(marklist)):
           print(str(i+1) + " " + str(marklist[i]) + " " + todolist[i])

def mark():
       print ('You saved the following to-do items:')
       liste ()
       y = input ('Which one you want to mark as completed: ')
       i = int(y)-1
       marklist[i] = marked
       print (str(todolist[i]) + ' is completed')


def archive():
       for i in range(0,len(marklist)-1):
           if marklist[i]=="[x]":
               todolist.remove(todolist[i])
               marklist.remove(marklist[i])
       print("You saved the following items: ")
       liste()
   
def command_input():
       while True:
           command=input("\nPlease enter a command [add, liste, mark, archive]: ")
           if command in commands:
               if command=="add":
                   add()
               elif command =="liste":
                   liste()
               elif command=="mark":
                   mark()
               elif command=="archive":
                   archive()
           else:
               print ('Please enter add, liste, mark, archive!')

command_input()
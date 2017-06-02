marklist = ["[]","[]","[]","[]","[]"]
todolist = ["apple","homework","milk","todolist","dog"]

def listing():
     print("You saved the following to-do items:")
     for i in range(0,len(marklist)):
         print(str(i+1) + " " + str(marklist[i]) + " " + todolist[i])

listing()


    


    

# To do list app in python
def app():
    print("Hi User welcome,Whats your task for today......")
    x=int(input("Enter no of tasks you want to add:"))
    for i in range(1,x+1):
        y=input(f"Enter your {i} task:"  )
        list.append(y)
    print(f"Your daily Task are {list} ")
    while True:
        print("Press 1->To add new task:")
        print("Press 2->To update task:")
        print("Press 3->To view your list:")
        print("Press 4->To delete your task:")
        print("Press 5->To exit from the app:")
        ch=int(input("Enter your choie:"))
        if(ch==1):
            add()
        if(ch==2):
            update()
        if(ch==3):
            view()
        if(ch==4):
            delete()
        if(ch==5):
            break 
def add():
    x=input("Enter your new task: ")
    list.append(x)
    print("---------Task added succesfully----------")
def update():
    x=input("Enter your task that you want to update: ")
    if x  in list:
        idx=list.index(x)
        up=input("Enter new task:")
        list[idx]=up
        print("---------Task updated succesfully----------")
    else:
        print("<<<<<<The task that you are trying to access is not in list>>>>") 
def view():
      print(f"Now Your daily Task are {list} ")  
def delete():
    x=input("Enter task that you want to delete:")
    list.remove(x)
    print("---------Task deleted succesfully----------") 
list=[] # empty list
app()

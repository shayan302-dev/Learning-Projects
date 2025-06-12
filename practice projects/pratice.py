to_do_list = []
while True:
    print("1. Add task")
    print("2. view task")
    print("3. remove task")
    print('4. Exit')
    select_task = int(input("Select the task: "))
    if select_task == 1:
        add = input("Enter the task: ")
        to_do_list.append(add)
        print("Task Added \n")

    elif select_task ==2:
        if not to_do_list:
            print("No Task Exists \n")
        else:
            for index , elements in enumerate(to_do_list,start=1):
                print(index,elements,"\n")

    elif select_task == 3:
        if not to_do_list:
            print("Nothing to Remove")
        else:
            print("Your tasks")
            for index,elements in enumerate(to_do_list,start = 1):
                print(index,elements)
            index = int(input("Enter the index of task you want to remove: "))
            if index <=1 <= len(to_do_list):
                remove =to_do_list.pop(index -1)
                print(f"Removed {remove} \n")
            else:
                print("Invalid task number \n")

    elif select_task ==4:
        print("Good bye")
        break
    else:
        print('Invaid task please select 1-4 \n')
            

 
    
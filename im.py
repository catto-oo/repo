#check chatgpt "python thing" chat for isntructions


task_list = ["task1","task2","task3","task4"]

menu = True
while menu == True: #add reorder list function
    print(' 1: Add a task \n 2: View tasks \n 3: Mark a task as completed \n 4: Remove a task \n 5: Exit')

    response = input('Please select a menu option: ')
        
    if response == '1':
        print('You want to add a task.')
        new_task = input('Enter a task: ')


        done = False
        while not done:
            try:
                new_task_num = int(input('Enter the order of the task in the list (1-' + str(len(task_list)+1) + '): '))
                if new_task_num > len(task_list)+1 or new_task_num <= 0:
                    print("That number is too big! Or maybe too small?")
                else:
                    task_list.insert(new_task_num - 1  , new_task)
                    print("Here's your new list:")
                    for task in task_list:
                        print(" " + str(task_list.index(task)+1) + ". " + task)
                    done = True

                    doneso = False
                    while not doneso:
                        quit_inquiry = input('\nWould you like to quit? Yes/No: ').lower()
                        if quit_inquiry: #checks if its not an empty string
                            if quit_inquiry[0] == 'y':
                                print('Goodbye!')
                                doneso = True
                                menu = False
                            elif quit_inquiry[0] == 'n':
                                print('\n \n \n \n \n \n \n')
                                doneso = True
                            else:
                                print('Please pick a valid response.')
                        else:
                            print("You didn't type anything.")
                    
            except ValueError: 
                print("You didn't enter a valid number.")


    elif response == '2':
        print('You want to view tasks.\n')
    elif response == '3':
        print('You want to mark a task as completed.\n')
    elif response == '4':
        print('You want to remove a task.\n')
    elif response == '5':
        print('You want to exit.')
        menu = False
    else:
        print('Please pick one of the numbers from the menu.\n')
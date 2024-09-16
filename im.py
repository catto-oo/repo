#check chatgpt "python thing" chat for isntructions


task_list = ["task1","task2","task3","task4"]

menu = True
while menu == True: #add reorder list function
    print(' 1: Add a task \n 2: View tasks \n 3: Mark a task as completed \n 4: Remove a task \n 5: Exit')

    response = input('Please select a menu option: ')
        
    if response == '1':
        print('You want to add a task.')
        new_task = input('Enter a task: ')
        try:
            new_task_num = int(input('Enter the order of the task in the list: '))
            task_list.insert(new_task_num - 1  , new_task)
            print("Here's your new list:")



        except ValueError: #I should add an error if the number is way more than the amount of items in the list like 78 and if its negative or 0
            print("That's not a number.") #this should return you to the beginning of 'try'

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
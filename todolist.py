#print menu to show user
def print_menu():
    print('Press 1 to add task')
    print('Press 2 to delete task ')
    print('Press 3 to view all tasks ')
    print('Press q to quit ')

tasks = []

def add_task():
    add_title = input('Please provide title of task: ')
    add_priority = input('Please provide priority of task: (high, low, medium)')
    taskdict = {"title": add_title, "priority": add_priority}
    tasks.append(taskdict)


def view_all_tasks():
    for (task) in tasks:
      print(f"{tasks.index(task)+1} . {task['title']} : {task['priority']} ")


def delete_task(): 
    view_all_tasks()    
    user_input = int(input('Enter item number to delete: '))
    del tasks[user_input-1]

user_input = ""

while user_input != 'q':
    print_menu()
    user_input = input('Enter your choice: ')
    if user_input == '1':
        add_task()
    elif user_input == '2':
        delete_task()
    elif user_input == '3':
        view_all_tasks()

#Show user all the tasks along with the index number of each task. 
#   User can then enter the index number of the task to delete the task. 
#Allow the user to view all the tasks in the following format:  
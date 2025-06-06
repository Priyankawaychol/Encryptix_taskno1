import json
import os

TODO_FILE= "todo_list.json"

def load_task():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    return []

def save_task(task):
    with open(TODO_FILE,"w", encoding="utf-8") as f:
        json.dump(task, f, indent=4)
        
def display_task(task):
    if not task:
        print("\n No tasks in your to-do list.\n")
        return
    print("\n Your TO DO LIST:")
    for i , task in enumerate(task,1):
        status="[x]" if task["completed"] else "[ ]"
        print(f"{i}.{status} {task['description']}")
    print()
    
def add_task(task):
    des=input("Enter a new task: ").strip()
    if des:
        task.append({"Description": des, "completed":False })
        print("TASK Added")
    else:
        print("Empty task not added")
        
def mark_task_completed(task):
    display_task(task)
    if not task:
        return
    try:
        num=int(input("enter the number of task is completed: "))
        if 1<=num<=len(task):
            task[num-1]["completed"]=True
            print("Task marked as completed")
        else:
            print("Invalid task number")    
    except ValueError:
        print("Please enter a valid number")
        
def delete_task(task):
    display_task(task)
    if not task:
        return
    try:
        num=int(input("enter the number of task is delete: "))
        if 1<=num<=len(task):
            removed=task.pop(num-1)
            print(f"Deleted task:'{removed['description']}")
        else:
            print("Invalid task number")    
    except ValueError:
        print("Please enter a valid number")

def main():
    task=load_task()
    while True:
        print("""
              TO DO LIST APPLICATION
              -----------------------
              1.View task
              2.Add new task
              3.Mark task as completed
              4.Delete task
              5.Exit
              """) 
        choice=input("Choose an option (1-5):").strip()
        if choice=='1':
            display_task(task)
        elif choice=='2':
            add_task(task)
            save_task(task)
        elif choice=='3':
            mark_task_completed(task)
            save_task(task)      
        elif choice=='4':
           delete_task(task)
           save_task(task)
        elif choice=='5':
            save_task(task)
            print("GOODBYE")
            break
        else:
            print("Invalid choice.Please select a valid option")
            
if __name__== "__main__" :
    main()   
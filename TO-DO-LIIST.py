def main ():
       tasks = []

       while True :
         print("\___To-Do list___") 
         print("1. Add a task") 
         print("2. View tasks") 
         print("3. Delete a task") 
         print("4. Exit") 

         choice = input("choose an option (1-4): ") 

         if choice == '1':   
              task = input("Enter the new task: ") 
              tasks.append(task)
              print("Task added successfully!")

         elif choice == '2':
              print("\nYour current tasks:")
              for index, task in enumerate(tasks, start=1):
                   print(f"{index}. {task}") 

         elif choice == '3':  
              task_num = int(input("Enter the task number to delete:"))  
              if 0 < task_num  <= len (tasks): 
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                    print("Invalid number.")
         elif choice == '4':  
                  print("Goodye!")
                  break
         else:
              print("Invalid option, please try again.")   
if __name__== "__main__":
       main()         
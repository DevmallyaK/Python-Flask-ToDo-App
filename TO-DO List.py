'''Personal To-Do list in Python'''

'''Write a program to build a simple To-Do list using Python which can perform following operations:

Accept
Display
Search
Delete
Update
Approach: Below is the approach to do the above operations:

Accept – This method takes details from the user like Task_name, serial_no, and time_start & time_finish for two different subjects.
# Method to enter new student details
def accept(self, Task_name, serial_no, time_start, time_finish ):
    # Creates a new class constructor
    # and pass the details
    ob = Student(Task, Serial, time_s, time_f )

    # list containing objects of student class
    ls.append(ob)
Display – This method displays the details of every Task.
# Function to display student details     
def display(self, ob):
    print("Name   : ", ob.Task)
    print("RollNo : ", ob.Serial)
    print("Marks1 : ", ob.time_s)
    print("Marks2 : ", ob.time_f)
    print("\n")    
Search – This method searches for a particular Task from the list of Task.
This method will ask the user for Serial number and then search according to the Serial number
# Search Function    
def search(self, rn):
    for i in range(ls.__len__()):
        # iterate through the list containing
        # Task object and checks through
        # Serial no of each object
        if(ls[i].Serial == rn):
            # returns the object with matching 
            # Serial number
            return i 
Delete – This method deletes the record of a particular Task with a matching Serial number.
# Delete Function                                  
def delete(self, rn):
    # Calls the search function 
    # created above
    i = obj.search(rn)  
    del ls[i]
Update – This method updates the Serial number of the Task.
This method will ask for the old Serial number and new Serial number. It will replace the old Serial number with new Serial number.
# Update Function   
def update(self, rn, No):
    # calling the search function
    # of student class
    i = obj.search(rn)
    ls[i].Serial = No'''

class ToDO:
    def __init__(self, name_Task, serial_number, time_started, time_finished):
        self.name_Task = name_Task
        self.serial_number = serial_number
        self.time_started = time_started
        self.time_finished = time_finished

    # Method to enter new student details
    def accept(self, Task_name, serial_no, time_start, time_finish):
        ob = ToDO(Task_name, serial_no, time_start, time_finish)
        ls.append(ob)

    # Function to display Task details
    def display(self, ob):
        print("Task Name   : ", ob.name_Task)
        print("Serial No : ", ob.serial_number)
        print("Start Time : ", ob.time_started)
        print("Finish Time : ", ob.time_finished)
        print("\n")

    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].serial_number == rn):
                return i

    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        serial = No
        ls[i].serial_number = serial


# Create a list to add Students
ls = []
# an object of Student class
obj = ToDO('', 0, 0, 0)

print("\nOperations used, ")
print("\n1.Accept Task details\n2.Display Task Details\n"
       "3.Search Details of a Task\n4.Delete Details of Task" 
       "\n5.Update Student Task\n6.Exit")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("Get food", 1, 2, 3)
obj.accept("Study", 2, 8, 1)
obj.accept("Exercise", 3, 6, 7)

# elif(ch == 2):
print("\n")
print("\nList of Task\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 3):
print("\n Task Found, ")
s = obj.search(2)
obj.display(ls[s])

# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])

# else:
print("Thank You !")
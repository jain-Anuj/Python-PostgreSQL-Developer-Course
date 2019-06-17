student_list=[]

def create_student():
    student_name = input("Enter the student name ")
    student_data = {'name':student_name,"marks": []}
    return student_data

def append_marks(student, mark):
    student["marks"].append(mark);

def avg_marks(student):
    length=len(student["marks"])
    if length==0:
        return 0
    total_sum=sum(student["marks"])
    return total_sum/length;

def student_details(student):
    print("Name of the student : "+student["name"])
    print("Marks of the student : {}".format(student["marks"]))
    print("Average marks : {}".format(avg_marks(student)))


def print_student_list(students):
    for student in students:
        student_details(student)

def menu():
    while 1:
        print("MENU :")
        print("1# Add a student")
        print("2# Add a mark to a student")
        print("3# print a list of student")
        print("4# Exit the Application")
        choice = int(input("Enter your choice "))

        if choice == 1:
            s=create_student()
            student_list.append(s)
        elif choice == 2:
            name=input("Enter the name of the student for whom you want to eneter the name : ")
            rep = int(input("Enter the total number of marks you want to enter : "))
            for s in student_list:
                if name == s["name"] :
                    for i in range(rep):
                        mark=int(input("Enter the mark : "))
                        s["marks"].append(mark)
        elif choice == 3:
            print_student_list(student_list)
        elif choice == 4:
            break
        else:
            print("Invalid Choice, retry")





menu()

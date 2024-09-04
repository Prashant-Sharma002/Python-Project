# addStudent
# updateStudent
# deleteStudent
# viewStudent
# Exit


# Storing the values
studentGrads = {

}
# Add Student Name and Grade
def addStudent( Name, Grade):
    studentGrads[Name]=Grade
    print(f"Added {Name} with a {Grade} ")
  


# Update Student Name and Grade
def updateStudent(Name, Grade):
    if Name in studentGrads:
        studentGrads[Name]=Grade
        print(f"{Name} With marks are updatd{Grade}")

    else:
        print(f"{Name} is not found")


# Delete Student Name and Grade
def  deleteStudent(Name):
    if Name in studentGrads:
        del studentGrads[Name]
        print(f"{Name} has been successfuly deleted")
    else: 
        print(f"{Name} is not found !")





# Diaplay Student Name and Grade
def  view_AllStudent():
    if studentGrads:
        for Name, Grade in studentGrads.items():
            print(f"{Name} : {Grade}")



    else:
            print("No student found/added")

def main():
    while True:
        print('\n .....Student Grades Management System.....')
        print("1.Add Student: ")
        print("2.Update Student: ")
        print("3.Delete Student: ")
        print("4.View Student: ")
        print("5.Exit: ")
        
        choice=int(input("Enter your choice= "))
        if choice==1:
            Name=input("Enter Student Name= ")
            Grade=int(input("Enter Student Garde= "))
            addStudent( Name, Grade)


        elif choice == 2:
             Name=input("Enter Student Name= ")
             Grade=int(input("Enter Student Garde= "))
             updateStudent(Name, Grade)
        
        elif choice == 3:
             Name=input("Enter Student Name= ")
             deleteStudent(Name)
             
        
        elif choice == 4:
            view_AllStudent()

            # Exit Student Grades Management System
        
        elif choice == 5:
            print("Your clossing the programe.......")
            break

        else:
            print("Invalid choice")
        
           
main()
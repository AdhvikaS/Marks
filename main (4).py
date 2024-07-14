#Adhvika

student={}

while True:
    name=str(input("Enter name of student "))
    if name=="done":
        break
    grade=float(input("Enter Marks "))
    student[name]=grade
    
if student:
    avg=sum(student.values())/len(student.values())
    highest=max(student.values())
    lowest=min(student.values())
    
    print(f"Average : {avg}")
    print(f"highest grade : {highest}")
    print(f"lowest grade : {lowest}")
    
else:
    print("No student data found")
    
    
    
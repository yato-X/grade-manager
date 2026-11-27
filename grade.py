def add_students():
    global name, subject1, subject2, subject3
    name= input("Enter your name: ")
    subject1= float(input("Enter your score for Mathematics: "))
    subject2= float(input("Enter your score for Scienc: "))
    subject3= float(input("Enter your score for English: "))
def calculate_average():
    average = float((subject1+subject2+subject3)/3)
    return average
average=calculate_average()
 
if(average>=90):
    Grade="A"
elif(average>=75):
    Grade="B"
elif(average>=60):
    Grade="C"
elif(average>=40):
    Grade="D"
elif(average<40 & average>0):
    Grade="NG"
elif(average>100):
    Grade="Error in average"
else:
    Grade="Error"
print(f"Name:n\{name} Average:\n{average:.2f} Grade:\n{Grade}")

name=input("enter the name of the student: ")
print("welcome", name)
study_hours=int(input("enter the number of hours you study per day: "))
if study_hours < 2:
    print("you need to study more")
elif study_hours >=6:
    print("maintaining a balance is important")

Assignment_status=input("have you completed your assignment?(yes/no): ")
if Assignment_status.lower()=="yes":
    print("assignment is completed ")
else:
    print("assignment is not completed: ") 

attendance=float(input("enter your attendance percentage"))
test_score=int(input("enter your test score out of 100: "))
if attendance >= 75 and test_score >= 80:
    print("you are doing well")
elif attendance >= 60 and test_score >= 60:
    print("good performance but there is room for improvement ")
elif attendance < 60 or test_score < 60:
    print("Needs improvment")
elif attendance <50:
    print("WARNING:YOUR ATTENDANCE IS LOW")
else:
    print("Maintain consistency in your performence ")
    
    
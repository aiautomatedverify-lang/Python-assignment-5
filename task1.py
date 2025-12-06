student_details = {
    "Alice":60,
    "Bob":80,
    "Charlie":90,
    "David":70,

}

user = input("Enter the student's name: ")
if user in student_details:
    print(user,"marks :",student_details[user])

else:
    print("Student Not Found")

#get student last name
last_name = input("What is your last name? :")

#end program if ZZZ entered 
if last_name == "ZZZ":
    exit()
    
#get student first name
first_name = input("What is your first name? :")

#get student gpa 
gpa = round(float(input("What is your GPA? :")),2)

#test student gpa 
if gpa >= 3.5:
    print("Congratulations! You have made the Dean's List!")
elif gpa>= 3.25:
    print("Congratulations! You have made the Honor Roll!")
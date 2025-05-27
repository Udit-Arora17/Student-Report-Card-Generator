print("Welcome to the student report card generator!")
print("1.Add Student Report\n" \
"2.View Reports\n" \
"3.Exit\n" \
"4.Delete Previous Records\n" \
"You can select numbers according to what do you want")
user=int(input("What do you want to do?\n"))
if user==1:
    name=input("Enter student name:")
    print("Enter marks for 3 subjects:")
    Eng=int(input("English:"))
    Maths=int(input("Maths:"))
    Science=int(input("Science:"))
    print(f"\nReport card for {name}: ")
    m=(Eng+Maths+Science)/3
    print(f"Average:{m}")
    print(f"Total:{(Eng+Maths+Science)}")
    def Grades(m):
        if m>90 or m==100:
            return("Grade:A+")
        elif m>80 or m==90:
            return("Grade:A")
        elif m>70 or m==80:
            return("Grade:B")
        elif m>60 or m==70:
            return("Grade:C")
        elif m>50 or m==60:
            return("Grade:D")
        elif m<50:
            return("Grade:F")
    Grade=(Grades(m))
    print(Grade)
    print("Data Saved Successfully")
    data=str(f"Name:{name}\nScience:{Science}\nMaths:{Maths}\nEnglish={Eng}\n{Grade}\nAverage={m}")
    with open ("Report_Card.txt","w") as g:
        g.write(data)
if user==2:
    with open ("Report_Card.txt","r") as z:
        read=z.read()
    print(read)
    if read=="":
        print("There are no records in the file")
if user==3:
    print("You are now free to do whatever you want")
if user==4:
    with open ("Report_Card.txt","w") as z:
      z.write("") #This deletes all the contents 
    print('All the previous records have been successfully deleted')
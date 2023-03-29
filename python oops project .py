#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Marksheet calculator
#class student-----Attribute--->>>name ,age,gender,seat number etc
# class marksheetdetails
class Student: 
    def __init__(self,Name,Age,Gender,class_,SeatNum,current_year):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
        self.class_=class_
        self.SeatNum=SeatNum
        self.current_year=current_year
   
    def viewprofile(self): # to display the input values
        print("Name:- ",self.Name)
        print("Age:- ",self.Age)
        print("Gender:- ",self.Gender)
        print("class_:- ",self.class_)
        print("SeatNum:-",self.SeatNum)
        print("current_year:-",self.current_year)

class Marksheetdetails: 
    #marks of particular subject
    def __init__(self, marks):
        self.marks = marks

        
    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self, total_marks):
        return (self.calculate_total() / total_marks) * 100

obj=Student("John", 28, "male", "12th","E088049","2012")
obj.viewprofile()
marks = (80, 85, 90, 75, 95)
marksheet1 = Marksheetdetails(marks)
total_marks = 500
print(f"{obj.Name} scored {marksheet1.calculate_total()} out of {total_marks} with {marksheet1.calculate_percentage(total_marks)}% who has appeard for exam in {obj.current_year}.")
obj1=Student("Madhuri", 28, "female", "12th","E021579","2013")
obj1.viewprofile()
marks = (50, 46, 97, 75, 95)
marksheet1 = Marksheetdetails(marks)
total_marks = 500
print(f"{obj1.Name} scored {marksheet1.calculate_total()} out of {total_marks} with {marksheet1.calculate_percentage(total_marks)}% who has appeard for exam in {obj1.current_year}.")
obj2=Student("Mayur", 30, "male", "12th","E078962","2009")
obj2.viewprofile()
marks = (87, 85, 98, 87, 95)
marksheet1 = Marksheetdetails(marks)
total_marks = 500
print(f"{obj2.Name} scored {marksheet1.calculate_total()} out of {total_marks} with {marksheet1.calculate_percentage(total_marks)}% who has appeard for exam in {obj2.current_year}.")


# In[ ]:





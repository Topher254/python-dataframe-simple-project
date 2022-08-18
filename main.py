# mission 3
# First we have to import the pandas library so that we can be able to use a dataframe
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn' Here we're getting rid of overwriting error in the dataframe after getting the input from the user
Name = str(input("Please Enter your Name here: "))
print("Let's calculate your weighted grades...")
# after importing the library, we create a dataframe using the dictionary dataframe function
df = pd.DataFrame.from_dict({
    'Activity': ['Discussions', 'Quizzes', 'Missions', 'Homework', 'Final_Project'],
    'Grade': ['Discussion_grade', 'Quiz_grade', 'Mission_grade', 'Homework_grade', 'Project_grade'],
    'Weight': [0.05, 0.35, 0.25, 0.10, 0.25],
    'Total_grade_per_activity': [0, 0, 0, 0, 0]
})
# uncomment the line below to check how the dataframe is displayed in tabular excel-like sheet
# print(df)
my_grade = list(df.Grade)  # here, I convert the grade elements from a dictionary to a list so that I can be able to add new data to it
Discussion_grade = float(input("Enter you total Discussion mark: "))
my_grade[0] = Discussion_grade
# I will prompt other activity input from the user then push it to the dataframe
Quiz_grade = float(input("Enter you total Quiz mark: "))
my_grade[1] = Quiz_grade

Mission_grade = float(input("Enter you total Mission mark: "))
my_grade[2] = Mission_grade

Homework_grade = float(input("Enter you total Homework mark: "))
my_grade[3] = Homework_grade

Final_Project = float(input("Enter you total Final project mark: "))
my_grade[4] = Final_Project


df.Grade[0] = my_grade[0]
df.Grade[1] = my_grade[1]
df.Grade[2] = my_grade[2]
df.Grade[3] = my_grade[3]
df.Grade[4] = my_grade[4]

# calculate total grade for discussion and other activity and overwrite it in the dataframe
Total_1 = (my_grade[0])*(df.Weight[0])
df.Total_grade_per_activity[0] = Total_1
Total_2 = (my_grade[1])*(df.Weight[1])
df.Total_grade_per_activity[1] = Total_2
Total_3 = (my_grade[2])*(df.Weight[2])
df.Total_grade_per_activity[2] = Total_3
Total_4 = (my_grade[3])*(df.Weight[3])
df.Total_grade_per_activity[3] = Total_1
Total_5 = (my_grade[4])*(df.Weight[4])
df.Total_grade_per_activity[4] = Total_5
# calculating the total grades
Overall_Total = Total_1 + Total_2 + Total_3 + Total_4 + Total_5
# Now lets check out our dataframe then print our overall grade
print("Here is a table containing all your grades")
print(df)
print(Name, ", our overall Grade is", Overall_Total, "Points")




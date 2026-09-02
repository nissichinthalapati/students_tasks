import csv
import os

CSV_FILE = "user_data.csv"

print("====================================")
print("       USER DATA COLLECTION")
print("====================================")

name = input("Enter your full name: ")
age = input("Enter your age: ")
college = input("Enter your college: ")
department = input("Enter your department: ")
email = input("Enter your email: ")
github = input("Enter your GitHub profile: ")
linkedin = input("Enter your LinkedIn profile: ")
skills = input("Enter your technical skills: ")
career_goal = input("Enter your career goal: ")

user_data = [
    name,
    age,
    college,
    department,
    email,
    github,
    linkedin,
    skills,
    career_goal
]

file_exists = os.path.exists(CSV_FILE)

with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Name",
            "Age",
            "College",
            "Department",
            "Email",
            "GitHub",
            "LinkedIn",
            "Skills",
            "Career Goal"
        ])

    writer.writerow(user_data)

print("\nUser data saved successfully!")
print(f"Data stored in: {CSV_FILE}")
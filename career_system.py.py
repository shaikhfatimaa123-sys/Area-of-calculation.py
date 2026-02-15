# AI Based Career Guidance and Skill Recommendation System

import openpyxl
import os

# Excel file ka naam (same folder me hona chahiye)
file_name = "career_data.xlsx"

# ===== Career Suggestion Function =====
def suggest_career(math, bio, bus, eng, interest):
    avg = (math + bio + bus + eng) / 4

    if interest.lower() == "medical" and bio >= 70:
        return "Medical Field (Doctor, Nurse, Pharmacist)"
    
    elif interest.lower() == "it" and math >= 70:
        return "IT Field (Software Engineer, AI, Data Scientist)"
    
    elif interest.lower() == "business" and bus >= 65:
        return "Business & Entrepreneurship (BBA, MBA)"
    
    elif interest.lower() == "arts":
        return "Arts & Media (Designer, Journalist, Artist)"
    
    elif avg >= 60:
        return "You can choose any general graduation field"
    
    else:
        return "Further improvement required"


# ===== Skill Recommendation =====
def recommend_skills(interest):
    if interest.lower() == "medical":
        return ["Biology", "Chemistry", "First Aid", "Research Skills"]
    elif interest.lower() == "it":
        return ["Python", "Programming", "AI Basics", "Problem Solving"]
    elif interest.lower() == "business":
        return ["Marketing", "Finance", "Communication", "Leadership"]
    elif interest.lower() == "arts":
        return ["Creativity", "Design", "Writing", "Photography"]
    else:
        return ["Time Management", "Communication", "Basic Computer Skills"]


# ===== Check File Exists =====
if not os.path.exists(file_name):
    print("❌ Error: Excel file nahi mili! File name check karo.")
    exit()

# ===== Load Excel File =====
wb = openpyxl.load_workbook(file_name)
sheet = wb.active

print("\n===== AI Career Guidance System =====\n")

# ===== Read Data from Excel =====
for row in sheet.iter_rows(min_row=2, values_only=True):
    name, math, bio, bus, eng, interest = row

    career = suggest_career(math, bio, bus, eng, interest)
    skills = recommend_skills(interest)

    print("Student Name:", name)
    print("Math:", math, "Bio:", bio, "Business:", bus, "English:", eng)
    print("Interest:", interest)
    print("Suggested Career:", career)
    print("Recommended Skills:", ", ".join(skills))
    print("-" * 40)
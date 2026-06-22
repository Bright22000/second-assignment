def analyze_age(dob_tuple):
    day, month, year = dob_tuple # current date
    current_day = 21
    current_month = 6
    current_year = 2026

    # calculating age in years, months and days
    age_in_years = current_year - year
    age_in_months = current_month - month
    age_in_days = current_day - day

    # adjusting the age in days if negative
    if age_in_days < 0:
        age_in_days += 30
        age_in_months -= 1

    # adjusting the age in months if negative
    if age_in_months < 0:
        age_in_months += 12
        age_in_years -= 1
    # life stage
    if age_in_years <= 10:
        stage = "Child"   
    elif age_in_years <= 19:
        stage = "Teen"  
    elif age_in_years <= 35:
        stage = "Young Adult" 
    elif age_in_years <= 64:
        stage = "adult"

    else:
       stage = "senior"

         
    # Return Report
    Report = (f"age: {age_in_years} years," 
    f"{age_in_months} months," 
    f"{age_in_days},days\n" 
    f"life stage: {stage}")

    return Report

# finding the oldest and youngest person in a list with loops

def compare_ages(person_list):
    oldest = person_list[0]
    youngest = person_list[0]
    for person in person_list:
        name, dob = person

    # an older pers will have a smaller birth year
        if dob[2] < oldest[1][2]:
            oldest = person
    # younger pers with a bigger birth year

        if dob[2] > youngest[1][2]:
            youngest = person
    return oldest, youngest

# family members (name, dob)
family_members = [("Dad", (17, 6, 1957)),
("Mom", (13, 3, 1968)),
("Big Sis", (15, 11, 1990)),
("mine", (28, 2, 1995)),
("little sis", (21, 2, 2007)),
("niece", (17, 4, 2021))]

# looping through each family member
for member in family_members:
    name, dob = member
    print(f"\n{name}'s Report")
    print(analyze_age(dob))

# comparing the different Ages
oldest_person , youngest_person = compare_ages(family_members) 
print("\noldest person:", oldest_person[0])
print("youngest person:", youngest_person[0])



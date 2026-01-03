# Simple study analysis logic for project foundation
def analyze_study_hours(study_hours):
    if study_hours < 2:
       return "Low study hours – needs improvement"
    elif study_hours < 4:
       return "Moderate study hours – acceptable"
    else:
       return "Good study hours – productive day"


if __name__ == "__main__":
print(analyze_study_hours(1))
print(analyze_study_hours(3))
print(analyze_study_hours(5))


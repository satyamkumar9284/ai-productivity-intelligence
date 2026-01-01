import csv

def analyze_day(study_hours):
    if study_hours < 2:
        return "Very Low Study – High Risk"
    elif study_hours < 4:
        return "Low Study – Needs Improvement"
    else:
        return "Good Study Level"


if __name__ == "__main__":
    with open("data/sample_days.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            study = float(row["study_hours"])
            result = analyze_day(study)
            print(f"Study: {study} hrs → {result}")

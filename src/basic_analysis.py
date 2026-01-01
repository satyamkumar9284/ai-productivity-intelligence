def analyze_day(study_hours, sleep_hours):
    if study_hours < 2:
        return "Very Low Study – High Risk"
    elif study_hours < 4:
        return "Low Study – Needs Improvement"
    else:
        return "Good Study Level"


if __name__ == "__main__":
    study = float(input("Enter study hours today: "))
    result = analyze_day(study)
    print("Analysis:", result)

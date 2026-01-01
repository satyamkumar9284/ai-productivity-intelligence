def analyze_day(study_hours):
    if study_hours < 2:
        return "Bad day"
    elif study_hours < 4:
        return "Okay day"
    else:
        return "Good day"


if __name__ == "__main__":
    print(analyze_day(1))
    print(analyze_day(3))
    print(analyze_day(5))

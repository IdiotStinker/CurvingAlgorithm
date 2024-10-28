def denominatorCurving():
    newGrades = []
    ogDenominator = int(input("What is the original denominator? "))
    newDenominator = int(input("What is the curved denominator? "))
    for grade in grades:
        newGrade = grade * ogDenominator / newDenominator
        newGrade = str(newGrade)[:4]
        newGrades.append(newGrade)
    
    return newGrades

def percentToDecimal():
    newGrades = []
    for grade in grades:
        grade /= 100
        newGrades.append(grade)

    grades = newGrades

grades = [14/15, 10/15, 6/15, 10/15, 14/15, 13/15]

print(denominatorCurving())
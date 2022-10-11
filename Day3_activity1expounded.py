name = input('Name of Student: ')
math = float(input('Grade in Math: '))
sci = float(input('Grade in Science: '))
eng = float(input('Grade in English: '))
ave = ((math+sci+eng)/3)
m = "Math"
s = "Science"
e = "English"
print("Average: ", ave)

if ave > 74:
    print("Congratulations! You passed the semester.")
    if math < 75:
        print("But you need to re-enroll", m, "subject.")
        if math < 75 or sci < 75:
            print("But you need to re-enroll", m, "and", s, "subject.")
    elif sci < 75:
        print("But you need to re-enroll", s, "subject.")
        if sci < 75 or eng < 75:
            print("But you need to re-enroll", s, "and", e, "subject.")
    elif eng < 75:
        print("But you need to re-enroll", e, "subject.")
        if eng < 75 or math < 75:
            print("But you need to re-enroll", e, "and", m, "subject.")
else:
    print("Sorry, you have failed this semester.")

def average(name, english, math, science):
    solve = int(math+english+science)/3
    print("{0}'s grade(english={1}, math={2}, science={3}, and the average is {4}"
          .format(name,english,math,science,round(solve)))

print();
average("John",85,91,97)
print();
average("Ana",85,91,97)
print();
average("Frank",85,91,97)
print("Ernie Pogi")

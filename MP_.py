while True:
     n1 = int(input("Enter First Number: "))
     n2 = int(input("Enter Second Number: "))
     sum = n1 + n2
     print("The sum of", n1, "and", n2, "is", sum)
     retry = input('Do you want to try again? Y/N:     ')
     if retry.lower()=='n':
          break
print('Thank You!')
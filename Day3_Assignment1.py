#show the bonus of an employee by asking the employees year in service and office
#the user will input number for years in service and the following office (IT, acct, hr)

name = input("Enter Employee Name: ")
yearsinService = int(input("Enter Years-in-Service: "))
office = input("Enter Office: ")

if office == "IT":
    if yearsinService >= 10:
        print("Hi", name, ", your bonus is 10000.")
    else:
        print("Hi", name, ", your bonus is 5000.")
elif office == "acct":
    if yearsinService >= 10:
        print("Hi", name, ", your bonus is 12000.")
    else:
        print("Hi", name, ", your bonus is 6000.")
elif office == "HR":
    if yearsinService >= 10:
        print("Hi ", name, ", your bonus is 15000.")
    else:
        print("Hi ", name, ", your bonus is 7500.")
else:
    print("Office does not exist.")

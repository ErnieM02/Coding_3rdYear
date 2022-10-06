#show the bonus of an employee by asking the employees year in service and office
#the user will input number for years in service and the following office (IT, acct, hr)

name = input("Enter Employee Name: ")
yearsinService = int(input("Enter Years-in-Service: "))
office = input("Enter Office: ")

if office == "IT" and "it":
    if yearsinService > 9:
        print("Hi", name,", your bonus is 10000.")
    else:
        print("Hi", name,", your bonus is 5000.")
elif office == "acct" and "Acct":
    if yearsinService > 9:
        print("Hi", name,", your bonus is 12000.")
    else:
        print("Hi", name,", your bonus is 6000.")
elif office == "HR" and "hr":
    if yearsinService > 9:
        print("Hi ", name, ", your bonus is 15000.")
    else:
        print("Hi ", name, ", your bonus is 7500.")
else:
    print("Office is not existing.")


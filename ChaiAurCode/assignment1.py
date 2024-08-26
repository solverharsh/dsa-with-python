# Classify a person's age group : child(<13),Teenagr(13-19),Adult(20-59),Senior(60+)

age = int(input("Provide the age: "))

# if age<13:
#     print("child")
# elif age>=13 and age<=20:
#     print("Teenager")
# elif age>=20 and age<=59:
#     print("Adult")
# else:
#     print("Senior")

if age<13:
    print("child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")
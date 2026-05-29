time = int(input("What time is it? "))
alarm1 = int(input("How many hours to the alarm? "))
alarm2 = (time + alarm1) % 24

print("The alarm will go off at " + str(alarm2) +".00")
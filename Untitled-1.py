print("How many minutes do you run during the day")
duration = int(input("How many minutes do you run during the day"))
if duration < 30: 
    print("You should run more!")
else: 
    print("Great job, keep it up!")    
nutrition = input("Are you eating healthy"). lower()
if "yes" in nutrition:
 print("That's amazing! You are eating very healthy.")
else:
 print("You should pay attention to your nutrition!")
sleep = int(input("How many hours do you sleep a day"))
if sleep < 8:
 print("You should sleep more.")
else:
 print("You should sleep less.")
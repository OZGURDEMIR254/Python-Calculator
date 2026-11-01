import random

start = int(input("Enter the first number: "))
end  = int(input("Enter the second number: "))

selected_number = random.randint(start, end)
print("The selected number is:", selected_number)
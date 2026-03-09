print("Hello GitHub!")
name = input("What's your name?")
print("Nice to meet you,",name)
count = len(name)
print("Your name has", count, "letters.")

while True:
    age = input("What's your age? ")
    try:
        age_num = float(age)
        break
    except ValueError:
        print("Please enter a valid number for age.")

if age_num <= 18:
        print("You cannot drink alcohol.")
else:
        drink = input("What do you wanna drink?")
        print("Enjoy your", drink + "!")

# Count from 1 to 5
for number in range(1, 6):
    print(number)

# Loop through a list
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print("I like", fruit)

def greet(name):
    return "Hello, " + name +"."
greeting = greet(name)
print(greeting,"Have a good day"+ "!")

print ("hello" + str (5))
name = "Alice"
print(name)
numbers = [1, 2, 3, 4, 5]
print(numbers[4])

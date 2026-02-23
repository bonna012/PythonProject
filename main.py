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
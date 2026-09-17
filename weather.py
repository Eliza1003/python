# PART 1: Ask for today's temprature
temprature = int(input("Enter tody's temprature in Celsius: "))
# PART 2: Decide between a jacket and a t-shirt

if temprature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a ", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today")
    print("Wear a", outfit)

# PART 2: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")

#PART 4: Add an umbrella reminder only if it is raining
if is_raining == "yes":
    print("Bring an umbrella")

# PART 5: Ask for the wind speed
wind_speed = int(input("enter the wind speed in km/h: "))

#PART 6: Decide whether a windbreaker is needed
if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("No windbreaker is needed over your", outfit)

# PART 7: Ask whether there are puddles over the ground
has_puddles = (input("Are there puddles on the ground? (yes/no): "))

# PART 8: Decide between boots or sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry")
    print("Wear", shoes)

# PART 9: This message always prints, no matter what was chosen above
print("")
print("Weather check complete!")
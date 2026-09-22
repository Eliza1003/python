# Smart School Day Planner

print("=== Smart School Day Planner===")
print("Answer 3 quick questions and I will plan your day!\n")

day   = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather   =("What is the weather? (sunny / rainy / cloudy):").strip().lower()
homework   = input("Is your homework done? (yes / no)").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)

# Topic 1 -- if-elif-else: classify the day
if day in ("Saturday", "Sunday"):
    print("Day type   : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type   : First day of the week. Pack your weekly planner.")
elif day == "Friday":
    print("Day type   : Last school day. Return library books today.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type   : Regular school day. stay focused!")
else:
    print("Day type   : Day not recongnised. Please check your spelling.")

    # Topic 2 -- AND operator: sunny AND homework done
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park - great weather and homework is done!")

# Topic 3 -- OR operator: rainy OR cloudy
if weather == "rainy" or weather =="cloudy":
    print("Weather tip : Pack your umbrella - it may get wet outside.")
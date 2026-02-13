"""
Author: <YOUR REAL FIRST AND LAST NAME>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # string
preferred_weight_kg = 20.5 # float
highest_reps = 25 # interger
membership_active = True # boolean

# Step c: Create a dictionary named workout_stats
workout_stats = {
"Alex": (30, 45, 20),
"Romaine": (25, 35, 40),
"Amoy": (40, 20, 30),
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[friend + "_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
workout_list = []

for friend, minutes in workout_stats.items():
    if "_Total" not in friend:
        workout_list.append(list(minutes))

print("Workout List:", workout_list)

# Step f: Slice the workout_list
print("\nYoga and Running minutes for all friends:")
for row in workout_list:
    print(row[:2])

print("\nWeightlifting minutes for last two friends:")
for row in workout_list[-2:]:
    print(row[2]) 

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if "_Total" in friend and workout_stats[friend] >= 120:
        name = friend.replace("_Total", "")
        print(f"\nGreat job staying active, {name}!")

# Step h: User input to look up a friend
name_input = input("\nEnter a friend's name: ")

if name_input in workout_stats:
    yoga, running, weightlifting = workout_stats[name_input]
    total = workout_stats[name_input + "_Total"]

    print(f"\n{name_input}'s workout stats:")
    print("Yoga:", yoga)
    print("Running:", running)
    print("Weightlifting:", weightlifting)
    print("Total minutes:", total)
else:
    print(f"Friend {name_input} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {}

for friend, minutes in workout_stats.items():
    if "_Total" in friend:
        name = friend.replace("_Total", "")
        totals[name] = minutes

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("\nFriend with highest total workout minutes:", highest)
print("Friend with lowest total workout minutes:", lowest)

"""
Author: Kiana Sepasian
Assignment: #1
"""

# Step b: Create 4 variables
# gym_member is a string
gym_member = "Alex Alliton"

# preferred_weight_kg is a float
preferred_weight_kg = 20.5

# highest_reps is an integer
highest_reps = 25

# membership_active is a boolean
membership_active = True

# Step c: Create a dictionary named workout_stats
# workout_stats is a dictionary where keys are strings and values are tuples of integers
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 25),
    "Taylor": (50, 40, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, activities in list(workout_stats.items()):
    total_minutes = sum(activities)
    workout_stats[friend + "_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# workout_list is a 2D list (nested list) of workout minutes
workout_list = []

for friend, activities in workout_stats.items():
    if not friend.endswith("_Total"):
        workout_list.append(list(activities))

# Step f: Slice the workout_list
# Extract yoga and running minutes for all friends
for row in workout_list:
    print("Yoga and Running:", row[:2])

# Extract weightlifting minutes for the last two friends
for row in workout_list[-2:]:
    print("Weightlifting:", row[2])

# Step g: Check if any friend's total >= 120
# Check if any friend's total workout minutes are >= 120
for friend, value in workout_stats.items():
    if friend.endswith("_Total") and value >= 120:
        name = friend.replace("_Total", "")
        print(f"Great job staying active, {name}!")

# Step h: User input to look up a friend
# User input to look up a friend
user_name = input("Enter friend's name: ")

if user_name in workout_stats:
    activities = workout_stats[user_name]
    total = workout_stats[user_name + "_Total"]
    
    print(f"{user_name}'s workout minutes:")
    print("Yoga:", activities[0])
    print("Running:", activities[1])
    print("Weightlifting:", activities[2])
    print("Total minutes:", total)
else:
    print(f"Friend {user_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
# Friend with highest and lowest total workout minutes

totals = {}

for friend, value in workout_stats.items():
    if friend.endswith("_Total"):
        name = friend.replace("_Total", "")
        totals[name] = value

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Highest total workout minutes: {highest_friend} ({totals[highest_friend]} minutes)")
print(f"Lowest total workout minutes: {lowest_friend} ({totals[lowest_friend]} minutes)")

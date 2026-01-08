import datetime
import random
import json
import os

def initialization():
    global streak
    global points
    global last_date
    global today
    global name
    global habit

    streak = 0
    points = 0
    last_date = None
    today = str(datetime.date.today())

    name = input("Hello! What is your name!\n")
    print(f"\nIt is nice to meet you, {name.title()}. Welcome to Eshaan Bhansali's Habit Builder. With the help of this program, you will work to build a habit of your choice.\n")

    habit = input("What habit would you like to build?\n").title()
    print("\nAwesome! Let's get started with tracking your habit!")

DATA_FILE = "habit_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
        name = data["name"]
        habit = data["habit"]
        streak = data["streak"]
        points = data["points"]
        last_date = data["last_date"]
    
    today = str(datetime.date.today())

    print("\n-----------------------------------")
    print(f"Welcome back, {name.title()}!")
    print(f"Habit: {habit}")
    print(f"Today is {today}")
    print("-----------------------------------\n")


    while True:
        restart = input("Would you like to reboot your habit builder?\n").strip().lower()

        if restart == "y" or restart == "n":
            break
        else:
            print("Invalid input. Please enter Y or N.\n")
    
    if(restart == 'y'):
        print("\nRebooting...")
        print("-----------------------------------\n.\n.\n.\n")
        initialization()

else:
    initialization()
    
    
if last_date == today:
    print("\nYou've already checked in today. Come back tomorrow!")
    exit()

while True:
    answer = input("Have you completed your habit today? (Y or N)\n").strip().lower()

    if answer == "y" or answer == "n":
        break
    else:
        print("Invalid input. Please enter Y or N.\n")

success_messages = [
    "Great job! Keep the momentum going!",
    "Another step forward!",
    "Consistency beats motivation. Well done!",
    "Proud of you. This is how habits stick."
]

fail_messages = [
    "No worries! Tomorrow is a fresh start.",
    "Progress isn’t linear. Keep going.",
    "One day doesn’t define you. Reset and refocus.",
    "You’ve got this. Let’s try again tomorrow."
]

if answer == "y":
    streak += 1
    points += 10

    if streak % 7 == 0:
        points += 20
        print("🔥 BONUS! 7-day streak achieved!")

    print("\n" + random.choice(success_messages))
else:
    streak = 0
    print("\n" + random.choice(fail_messages))

data = {
    "name": name,
    "habit": habit,
    "streak": streak,
    "points": points,
    "last_date": today
}

with open(DATA_FILE, "w") as file:
    json.dump(data, file)

print("\n========== DAILY SUMMARY ==========")
print(f"Habit: {habit}")
print(f"Completed Today: {'Yes' if answer == 'y' else 'No'}")
print(f"Current Streak: {streak}")
print(f"Total Points: {points}")
print("==================================\n")

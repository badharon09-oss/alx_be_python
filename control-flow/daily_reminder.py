# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority
match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority.")

# Check if it is time-bound
if time_bound == "yes":
    print("This task requires immediate attention today!")

# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Your task '{task}' is LOW priority."
    case _:
        reminder = f"Priority for task '{task}' is not recognized."

# Adjust reminder if task is time-sensitive
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Output the customized reminder
print(reminder)

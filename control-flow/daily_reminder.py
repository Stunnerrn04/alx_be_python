# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority
match priority:
    case 'high':
        priority_message = "This task is of high priority."
    case 'medium':
        priority_message = "This task is of medium priority."
    case 'low':
        priority_message = "This task is of low priority."
    case _:
        priority_message = "Unknown priority level."

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    time_bound_message = "This requires immediate attention today!"
else:
    time_bound_message = "This does not require immediate attention today."

# Provide a customized reminder
print(f"Task: {task}")
print(f"{priority_message} {time_bound_message}")

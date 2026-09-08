from datetime import datetime

def validate_task_title(title):
    if not title or not title.strip():
        print("Error: Task cannot be empty")
        return False
    if len(title) > 50:
        print("Error: Task title must be 50 characters or less.")
        return False
    return True

def validate_task_description(description):
    if len(description) > 200:
        print("Error: Task description must be 200 characters or less")
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.striptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return False
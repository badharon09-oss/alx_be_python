from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format it as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days):
    # Get current date
    current_date = datetime.now()
    # Add the number of days
    future_date = current_date + timedelta(days=days)
    # Format future date as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date (after {days} days): {formatted_future_date}")

def main():
    # Part 1: Show current datetime
    display_current_datetime()

    # Part 2: Ask user for days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

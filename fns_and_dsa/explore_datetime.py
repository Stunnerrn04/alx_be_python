from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the current date and time
    print("Current date and time:", formatted_date)

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    # Prompt the user for the number of days
    days = int(input("Enter the number of days: "))
    
    # Calculate the future date by adding the number of days to the current date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print("Future date:", formatted_future_date)

def main():
    """
    Main function to execute the script functionalities
    """
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()

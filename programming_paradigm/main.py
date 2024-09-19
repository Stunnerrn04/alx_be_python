# main.py

from robust_division_calculator import safe_divide

def main():
    print("Division Calculator")
    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")
    
    # Call the safe_divide function
    result = safe_divide(numerator, denominator)
    
    # Print the result or error message
    print(result)

if __name__ == "__main__":
    main()

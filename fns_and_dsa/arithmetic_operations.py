def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

# Example usage
if __name__ == "__main__":
    result = perform_operation(10, 5, 'add')
    print(f"Addition result: {result}")
    
    result = perform_operation(10, 5, 'subtract')
    print(f"Subtraction result: {result}")
    
    result = perform_operation(10, 5, 'multiply')
    print(f"Multiplication result: {result}")
    
    result = perform_operation(10, 0, 'divide')
    print(f"Division result: {result}")
    
    result = perform_operation(10, 5, 'divide')
    print(f"Division result: {result}")
    
    result = perform_operation(10, 5, 'invalid')
    print(f"Invalid operation result: {result}")

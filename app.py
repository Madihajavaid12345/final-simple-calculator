import streamlit as st

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app interface
st.title('Simple Calculator')

# Take input numbers from the user
num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

# Select operation from a dropdown
operation = st.selectbox('Select operation', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

# When the user clicks the button, calculate the result
if st.button('Calculate'):
    if operation == 'Addition':
        result = add(num1, num2)
    elif operation == 'Subtraction':
        result = subtract(num1, num2)
    elif operation == 'Multiplication':
        result = multiply(num1, num2)
    elif operation == 'Division':
        result = divide(num1, num2)
    
    # Display the result
    st.write('Result:', result)

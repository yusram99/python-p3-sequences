#!/usr/bin/env python3

# def print_fibonacci(length):
def print_fibonacci(length):
    # Initialize with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]  

    while len(fibonacci_sequence) < length:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)

    print(fibonacci_sequence)

# Testing the function
print_fibonacci(9)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]

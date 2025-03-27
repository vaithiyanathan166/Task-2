#2 ) To create a pyramid of numbers from 1 to 20 using a For  loop

def print_number_pyramid(n):
    current_number = 1
    for i in range(1, n+1):
        # Print spaces for pyramid alignment
        print(' ' * (n - i), end='')
        
        # Print numbers in the current row
        for j in range(i):
            if current_number <= n:
                print(current_number, end=' ')
                current_number += 1
        print()  # Move to the next line

# Print a pyramid with numbers from 1 to 20
print_number_pyramid(20)


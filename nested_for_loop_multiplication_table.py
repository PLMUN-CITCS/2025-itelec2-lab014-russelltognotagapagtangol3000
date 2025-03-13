# Nested for loop to print a multiplication table

# Outer loop for rows (1 to 5)
for i in range(1, 6):
    # Inner loop for columns (1 to 5)
    for j in range(1, 6):
        # Calculate the product
        product = i * j
        # Print the product with formatting (aligned properly)
        print(f"{product:4}", end="")  
    # Print a new line after each row
    print()

def is_prime(num):
    """Returns True if num is prime, False otherwise."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  # Optimized: Only check up to the square root
        if num % i == 0:
            return False
    return True

# Get user input
n = int(input("Enter the number: "))

# Handle the number itself if it's less than 1
if n < 1:
    print("Please enter a positive integer greater than 0.")
else:
    print(f"\nFactors of {n} and their classification:")
    
    # Loop through all possible factors up to n
    for i in range(1, n + 1):
        if n % i == 0:
            if i == 1:
                print(f"{i} -> Neither (Unit)")
            elif is_prime(i):
                print(f"{i} -> Prime")
            else:
                print(f"{i} -> Composite")

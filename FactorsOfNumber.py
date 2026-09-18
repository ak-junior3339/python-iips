# python script to calculate factors adn identimy prime ones
factors = [] 
prime_factors = []
def isprime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
def factor(num):
    global factors, prime_factors

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

            if isprime(i):
                prime_factors.append(i)

factor(12)
print("All factors are : ",factors)
print("Which of it prime are : ",prime_factors)

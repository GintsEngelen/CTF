def prime_factors(n):
    factors = []
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Divide n by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors

# Input a number
num = int(input("Enter a number: "))

if num < 2:
    print("Prime factors are not defined for numbers less than 2.")
else:
    factors = prime_factors(num)
    print("Prime factors of", num, "are:", factors)

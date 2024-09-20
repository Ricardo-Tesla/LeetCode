def countPrimes(n: int) -> int:
    if n <= 2:
        return 0

    # Initialize a boolean array
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    # Sieve of Eratosthenes
    for p in range(2, int(n**0.5) + 1):
        if isPrime[p]:
            for multiple in range(p * p, n, p):
                isPrime[multiple] = False

    # Count primes
    return sum(isPrime)

# Example usage
n = 10
print(countPrimes(n))  # Output: 4

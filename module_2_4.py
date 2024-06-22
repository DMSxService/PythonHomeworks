numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
for i in range(0, len(numbers)):
    element = numbers[i]
    if element == 0 or element == 1 :
        continue
    for j in range(2, element):
        is_prime = not(element % j)
        if is_prime:
            not_primes.append(element)
            break
    if not is_prime :
        primes.append(element)
print(primes)
print(not_primes)
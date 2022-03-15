def main():
    primes = [2]
    sum = 2
    # Going up to 100000 only since 10^6 takes too long and we know that after 100000, max possible length < 10
    for i in range(3, 100000, 2):
        if(is_prime(i, primes)):
            primes.append(i)

    result = Prime_and_l()
    for i in range(len(primes)):
        pi = Prime_and_l()
        sum_j = 0
        for j in range(i, len(primes)):
            sum_j += primes[j]
            if (sum_j > 1000000):
                break
            elif(is_prime(sum_j, primes)):
                pi = Prime_and_l(sum_j, j - i + 1)
        if (pi.length > result.length):
            result = pi
    print(result.nb)
    
class Prime_and_l:
    def __init__(self, nb=0, length=0):
        self.nb = nb
        self.length = length

def is_prime(n, prime_list):
    for p in prime_list:
            if n % p == 0:
                return False
    return True

if __name__ == "__main__":
    main()
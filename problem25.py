import functools

@functools.lru_cache() #
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    i = 0
    nb = fibonacci(i)
    while(len(str(nb)) < 1000):
        i += 1
        nb = fibonacci(i)
    print(i)

if __name__ == "__main__":
    main()
def main():
    nb = 2**1000
    sum = 0
    for i in range(len(str(nb))):
        sum += nb // 10**i % 10
    print(sum)

if __name__ == "__main__":
    main()
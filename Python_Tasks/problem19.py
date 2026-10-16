# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    X = int(input("Enter the number of shoes: "))
    shoe_sizes = list(map(int, input("Enter shoe sizes: ").split()))

    inventory = Counter(shoe_sizes)

    N = int(input("Enter the number of customers: "))
    total_earnings = 0

    for _ in range(N):
        size, price = map(int, input("Enter shoe size and price: ").split())

        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1

    print(total_earnings)

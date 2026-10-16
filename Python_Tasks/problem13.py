# Problem: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    M = int(input("Enter the number of elements in set M: "))
    set_M = set(map(int, input("Enter elements of M: ").split()))

    N = int(input("Enter the number of elements in set N: "))
    set_N = set(map(int, input("Enter elements of N: ").split()))

    result = sorted(set_M.symmetric_difference(set_N))

    for num in result:
        print(num)

# Problem: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input("Enter n and m: ").split())
    array = list(map(int, input("Enter array elements: ").split()))
    A = set(map(int, input("Enter elements of set A: ").split()))
    B = set(map(int, input("Enter elements of set B: ").split()))

    happiness = 0

    for num in array:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1

    print(happiness)

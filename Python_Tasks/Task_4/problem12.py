# Problem: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_heights = set(array)
    return sum(unique_heights) / len(unique_heights)

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the heights separated by spaces: ").split()))
    result = average(arr)
    print(result)
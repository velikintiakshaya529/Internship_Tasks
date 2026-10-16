# Problem: What's Your Name?
# HackerRank: https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input("Enter a string1:")
    last_name = input("Enter a string2:")
    print_full_name(first_name, last_name)
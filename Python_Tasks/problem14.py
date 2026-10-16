# Problem: Set .add()
# HackerRank: https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input("Enter the number of country stamps: "))

    countries = set()

    for i in range(n):
        country = input("Enter country name: ")
        countries.add(country)

    print(len(countries))

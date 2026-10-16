# Problem: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input("Enter a string: ")
    i, c = input("Enter position and character: ").split()
    result = mutate_string(s, int(i), c)
    print(result)


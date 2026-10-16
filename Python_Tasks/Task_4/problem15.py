
# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input("Enter the number of words: "))

    words = []
    for i in range(n):
        word = input("Enter a word: ")
        words.append(word)

    unique_words = list(dict.fromkeys(words))

    print(len(unique_words))

    for word in unique_words:
        print(words.count(word), end=" ")

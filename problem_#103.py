"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
def solution(string, char_set):
    string_len = len(string)
    char_set_len = len(char_set)

    for i in range(string_len - char_set_len+1):
        print(string[i:i+char_set_len])


string = 'figehaeci'
char_set = ['a', 'e', 'i']

solution(string, char_set)

# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word: str, anagram: str):
    count = len(anagram)
    for letter in word:
        if letter in anagram:
            count -= 1
    if count == 0:
        return True
    else:
        return False


fun = find_anagram("vaa", "ava")
print(fun)




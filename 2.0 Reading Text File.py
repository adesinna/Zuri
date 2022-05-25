# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        return file.read()


def count_words():
    text = read_file_content("story.txt")
    text_lower = text.lower()
    replacement = {
        'students.': 'students',
        'question.': 'question',
        'instead,': 'instead',
        'asked,': 'asked',
        'holding?': 'holding',
        'water,': 'water',
        'face,': 'face',
        '\nas': 'as',
        '\ninstead': 'instead',


    }

    for key, value in replacement.items():
        text_lower = text_lower.replace(key, value)

    final_dict = {}

    contents = text_lower.split(' ')
    for word in contents:
        if word == '':
            index_word = contents.index(word)
            contents.pop(index_word)

    for word in contents:
        final_dict[word] = contents.count(word)

    return final_dict


x = count_words()
print(x)







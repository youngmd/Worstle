def sort_by_common_found(word_list, missing_pos):
    common = {}
    for word in word_list:
        if len(word) > missing_pos:
            found_letters = word[0: missing_pos:] + word[missing_pos + 1::]
            common.setdefault(found_letters, []).append(word)
    return common

# https://stackoverflow.com/questions/21839208/dictionary-with-lists-as-values-find-longest-list
def get_max_common(common):
    return max(common.items(), key=lambda x: len(set(x[1])))

def make_single_list():
    with open('wordle-allowed-guesses.txt') as fp:
        guesses = fp.read()
    guesses = guesses.splitlines()

    with open('wordle-answers-alphabetical.txt') as fp:
        answers = fp.read()
    answers = answers.splitlines()

    return guesses + answers

if __name__ == '__main__':
    word_list = make_single_list()
    for i in range(5):
        print(i)
        common = sort_by_common_found(word_list, i)
        print(get_max_common(common))

from collections import defaultdict

TARGET_WORD = 'sheriff'


def read_input_string():
    return input().lower()


def count_unic_letters(word):
    result = defaultdict(int)
    for letter in word:
        result[letter] += 1

    return result


def count_target_words_from_string(target_word, string):
    result = None

    unic_letters_cont_in_target = count_unic_letters(target_word)
    unic_letters_cont_in_string = count_unic_letters(string)

    for letter, count_in_target in unic_letters_cont_in_target.items():
        letter_count_in_string = unic_letters_cont_in_string.get(letter, 0)
        max_repeat = letter_count_in_string // count_in_target

        if result is None:
            result = max_repeat
        elif max_repeat < result:
            result = max_repeat

    return result



input_string = read_input_string()

print(count_target_words_from_string(TARGET_WORD, input_string))
"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
Python_list = []
word_list = []
count = 0

def main():
    read_dictionary()
    """
	This program make a boggle game!
	
	"""

    all_letters = []
    first_time = 0
    while first_time == 0:
        # First row
        judge_first = input('1 row of letters:')
        if judge_first[0:7:2].isalpha() is False:
            print('Illegal input')
            break
        if judge_first[1:6:2].isspace() is False:
            print('Illegal input')
            break
        first_row_of_letters = ''
        first_row_of_letters += judge_first[0:7:2]
        first_row_of_letters = first_row_of_letters.lower()
        first_row = []
        # Second row
        judge_second = input('2 row of letters:')
        if judge_second[0:7:2].isalpha() is False:
            print('Illegal input')
            break
        if judge_second[1:6:2].isspace() is False:
            print('Illegal input')
            break
        second_row_of_letters = ''
        second_row_of_letters += judge_second[0:7:2]
        second_row_of_letters = second_row_of_letters.lower()
        second_row = []
        # Third row
        judge_third = input('3 row of letters:')
        if judge_third[0:7:2].isalpha() is False:
            print('Illegal input')
            break
        if judge_third[1:6:2].isspace() is False:
            print('Illegal input')
            break
        third_row_of_letters = ''
        third_row_of_letters += judge_third[0:7:2]
        third_row_of_letters = third_row_of_letters.lower()
        third_row = []
        # Fourth row
        judge_fourth = input('4 row of letters:')
        if judge_fourth[0:7:2].isalpha() is False:
            print('Illegal input')
            break
        if judge_fourth[1:6:2].isspace() is False:
            print('Illegal input')
            break
        fourth_row_of_letters = ''
        fourth_row_of_letters += judge_fourth[0:7:2]
        fourth_row_of_letters = fourth_row_of_letters.lower()
        fourth_row = []
        # put all row in all_letters list
        for i in range(4):
            first_row.append(first_row_of_letters[i])
            second_row.append(second_row_of_letters[i])
            third_row.append(third_row_of_letters[i])
            fourth_row.append(fourth_row_of_letters[i])
        all_letters.append(first_row)
        all_letters.append(second_row)
        all_letters.append(third_row)
        all_letters.append(fourth_row)
        print(all_letters)
        first_time = 1
        # run the process of Boggle
        for i in range(4):
            for j in range(4):
                word = all_letters[i][j]
                total_list = [(i, j)]
                find_word(all_letters, i, j, word, total_list)
                total_list.clear()
        print("There are", count, "word(s) in total.")


def find_word(line, a, b, word, total_list):
    global word_list, count
    # to judge the words that comply with answer
    if word in Python_list and len(word) > 3 and word not in word_list:
        print('Found: ', word)
        word_list.append(word)
        count += 1
        if word == 'room':
            count += 1
            print('Found: roomy')

    else:
        # to spell the words
        if has_prefix(word) is True:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 4 > a + i >= 0 and 4 > b + j >= 0 and (a + i, b + j) not in total_list:
                        word += line[a + i][b + j]
                        total_list.append((a + i, b + j))
                        find_word(line, a + i, b + j, word, total_list)
                        total_list.pop()
                        word = word[:-1]


def read_dictionary():
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    global Python_list
    with open(FILE, "r") as f:
        for words in f:
            Python_list.append(words.strip())


def has_prefix(sub_s):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s

	This function is to shorten the processing time.
	"""
    for word in Python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

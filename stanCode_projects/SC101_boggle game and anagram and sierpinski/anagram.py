"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop
Python_list = []


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        word_input = input('find anagram for: ')
        word_input = word_input.lower()

        if str(word_input) is '-1':
            break

        else:
            find_anagrams(word_input)


def read_dictionary():
    global Python_list
    with open(FILE, "r") as f:
        for data in f:
            data = data.strip()
            Python_list.append(data)


def find_anagrams(s):
    count_lst = []
    anagram_lst = []
    find_anagrams_helper(s, [], [], count_lst, anagram_lst)
    print(sum(count_lst), "anagram:", anagram_lst)


def find_anagrams_helper(s, word, previous_word, count_lst, anagram_lst):
    if len(word) == len(s):
        ans = ''
        for i in range(len(word)):
            ans += word[i]
        if ans in Python_list:
            if ans not in previous_word:
                previous_word.append(ans)
                print('Searching...')
                print('Found:' + ans)
                count_lst.append(1)
                anagram_lst.append(ans)

    else:
        if has_prefix(word) is True:

            for i in range(len(s)):
                if s[i] not in word:
                    word.append(s[i])
                    # if has_prefix(word) is False:
                    #     break
                    find_anagrams_helper(s, word, previous_word, count_lst, anagram_lst)
                    word.pop()
                else:

                    if s[i] in s[0:i]:
                        word.append(s[i])
                        # if has_prefix(word) is False:
                        #     break
                        find_anagrams_helper(s, word, previous_word, count_lst, anagram_lst)
                        word.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:

    """
    best_ans = ''
    for j in range(len(sub_s)):
        best_ans += sub_s[j]
    for word in Python_list:
        if word.startswith(str(best_ans)) is True:
            return True
    return False
    # for i in Python_list:
    #     if str(Python_list[i]).startswith(sub_s) is False:
    #         break
    #     elif str(Python_list[i]).startswith(sub_s) is True:
    #         pass
    pass


if __name__ == '__main__':
    main()

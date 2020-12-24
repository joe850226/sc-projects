"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
biggest_num = 0
num = 0


def main():
    print(find_largest_digit(12345))  # 5
    print(find_largest_digit(281))  # 8
    print(find_largest_digit(6))  # 6
    print(find_largest_digit(-111))  # 1
    print(find_largest_digit(-9453))  # 9


def find_largest_digit(n):
    """
    :param n:
    :return:
    """
    global num, biggest_num
    if n == 0:
        if num > biggest_num:
            print(num)
        else:
            print(biggest_num)
        biggest_num = 0
        num = 0

    else:
        if n < 0:
            n = n * -1
            find_largest_digit(n)
        else:
            if n % 10 == 0:
                if num > biggest_num:
                    biggest_num = num
                num = 0
                find_largest_digit(n / 10)
            else:
                n -= 1
                num += 1
                find_largest_digit(n)

    pass


if __name__ == '__main__':
    main()

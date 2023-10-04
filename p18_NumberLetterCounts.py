letter_dict = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:'seven',
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"hundred",
    1000:"one thousand"
}

def counting(word):
    temp = 0
    for items in word:
        if items.isalpha():
            temp += 1
    return temp


def count_letters():
    fin = 0
    fin_string = []
    for i in range(1,1001):
        # print(i)
        if i <= 20:
            fin += counting(letter_dict[i])
        if 21 <= i <= 100:
            if i in letter_dict.keys():
                fin += counting(letter_dict[i])
                # 100 is stored as hundred but is represented as one hundred
                if i == 100:
                    fin += 3
            else:
                fin += counting(letter_dict[i - ((i)%10)])
                fin += counting(letter_dict[i % 10])
                letter_dict[i] = (letter_dict[i - ((i)%10)]+letter_dict[i%10])
                # print(letter_dict)
        if 1000 > i > 100:
            if i % 100 == 0 :
                fin += counting(letter_dict[i//100])
                fin += counting(letter_dict[100])
                letter_dict[i] = letter_dict[i//100]+letter_dict[100]
            else:
                fin += counting(letter_dict[i-(100*(i//100))])
                fin += counting(letter_dict[i//100])
                # no of letters in "hundredand"
                fin += 10
                letter_dict[i] = letter_dict[i//100]+"hundredand"+letter_dict[i-(100*(i//100))]
        elif i == 1000:
            fin += counting(letter_dict[i])

    # print(letter_dict)
    print("*******")
    print(fin)

if __name__ == "__main__":
    count_letters()
    sum_ = 0
    for nos,items in letter_dict.items():
        sum_ += counting(items)
        print(nos,items)
    print(sum_)


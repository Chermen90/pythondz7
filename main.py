'''''''''
user_song = input('Введите песенку: ')
def check_rhyme(song):
    split_song = song.split(' ')
    num_of_vowels = []
    for i in split_song:
        vowels = sum(letter in "аеёиуыои" for letter in i.lower())
        num_of_vowels.append(vowels)
    if len(set(num_of_vowels)) == 1:
        return print('Парам пам-пам')
    else: return print('Пам парам')


#пара-ра-рам рам-пам-папам па-ра-па-да
check_rhyme(user_song)
'''''''''



def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печатаем заголовок таблицы с номерами столбцов
    print("     ", end="")
    for j in range(1, num_columns + 1):
        print("{:>6}".format(j), end="")
    print()
    print("  +", "-" * (6 * num_columns), "+")
    for i in range(1, num_rows + 1):
        print("{:>2} |".format(i), end="")
        for j in range(1, num_columns + 1):
            print("{:>6}".format(operation(i, j)), end="")
        print()
    print("  +", "-" * (6 * num_columns), "+")

def multiply(i, j):
    return i * j

print_operation_table(multiply, num_rows=4, num_columns=5)
input_string = input("Please enter two words: ")

word_1 = input_string.split()[0]
word_2 = input_string.split()[1]

string_1 = '! %s %s ?' % (word_1[::-1].upper(), word_2[::-1].title())
string_2 = '! {} {} ?'.format(word_1[::-1].upper(), word_2[::-1].title())
string_3 = f'1 {word_1[::-1].upper()} {word_2[::-1].title()} ?'

source_file = open('file.txt', 'w')
print(input_string, string_1, string_2, string_3, sep='<<<>>>', file=source_file)
source_file.close()

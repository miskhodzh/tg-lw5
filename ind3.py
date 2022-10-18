word = input('Введите слово >>> ')
n = int(input('Введите номер символа >>>'))

word = word.replace(word[2], '')
word = word.replace(word[n], '')

print(word)
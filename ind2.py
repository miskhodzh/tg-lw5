sentence = input('Введите предложение >>> ')

for x in range(len(sentence)):
    if sentence[x] == 'а':
        print(x)
        break
    elif x == len(sentence) - 1:
        print('Символ "а" в строке не найден')
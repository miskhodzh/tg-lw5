word = input('Введите слово >>> ')
n = int(input('Введите номер символа >>>'))

if n > 3:
    word = word[:2]+word[3:n]+word[n+1:]
elif n < 3:
    word = word[:n]+word[n+1:2]+word[3:]

print(word)
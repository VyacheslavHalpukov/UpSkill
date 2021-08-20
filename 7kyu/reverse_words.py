def reverse_words(text):
    list = text.split(' ')[::-1]
    new_text = ' '.join(list)[::-1]
    return new_text

print(reverse_words('Hello World!'))


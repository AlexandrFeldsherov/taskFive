# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

def del_some_words(text_new):
    text_new = list(filter(lambda x: 'абв' not in x, text_new.split()))
    return " ".join(text_new)

my_text='абвгдейка - это передача'
text_new = del_some_words(my_text)
print(f"{my_text} => {text_new}")
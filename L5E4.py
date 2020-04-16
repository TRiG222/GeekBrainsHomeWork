from googletrans import Translator  # первая попавшаяся библиотека переводчика

translator = Translator()

new_f = []
with open('text_4.txt') as my_f:
    for i in my_f:  # перевод первоначального файла
        my_l = i.split(' ', 1)
        translations = translator.translate(my_l[0], dest='ru')
        new_f.append(translations.text + ' ' + my_l[1])

with open('text_4part2.txt', 'w') as my_fnew:  # запись в новый файл
    my_fnew.writelines(new_f)

with open('text_4part2.txt') as my_fnew:  # чтение нового файла
    print(my_fnew.read())

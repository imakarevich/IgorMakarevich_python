# Исходное предложение..
sentense = "Не знаю, как там в Лондоне, я не была. Может, там собака —"\
           " друг человека. А у нас управдом — друг человека!" 

# 1.Посчитать количество символов.
characters = len(sentense)
print("Шаг.1 - Количество символов: ", characters)

# 2.Развернуть строку. Python yes -> sey nohtyP.
back_sentense_characters = sentense[::-1]
print("Шаг.2 - Развернутая строка по символам: ", back_sentense_characters)

# 3.Сделать каждое слово с большой буквы.
words_uppercase = sentense.title()
print("Шаг.3 - Каждое слово с большой буквы: ", words_uppercase)

# 4.Сделать весь текст прописными буквами.
characters_lower = sentense.lower()
print("Шаг.4 - Весь текст прописными буквами: " + characters_lower)

# 5.Найти число вхождений "нд", "ам", "о" в строку.
string_in_sentence_count_1 = sentense.count("нд",0,)
string_in_sentence_count_2 = sentense.count("ам",0,)
string_in_sentence_count_3 = sentense.count("о",0,)
print('Шаг.5 - Число вхождений "нд": ', string_in_sentence_count_1, \
      ', \"ам\": ', string_in_sentence_count_2, ', "о": ', string_in_sentence_count_3)

# 6. Собственные упражнения.
print("Шаг.6 - Собственные упражнения:\n")
print("----------------------------------------------------------------------------------")
print("Повторение строки 2 раза:\n\n", sentense*2)
print("----------------------------------------------------------------------------------")
print("Просто срез с шагом 2:\n\n", sentense[0::2])
print("----------------------------------------------------------------------------------")
print("Просто конкатенация срезов + .upper():\n")
print((sentense[82:90] + sentense[8:12] + sentense[49:57]).upper())
print("----------------------------------------------------------------------------------")
print("Удаление '.', '!', '—', ',' при помощи .replace():\n")
sentense_without_punctuation = sentense.replace(",", "").replace("—","").replace("!"\
                                   ,"").replace(".","").replace("  "," ")
print(sentense_without_punctuation)
print("----------------------------------------------------------------------------------")
print("Просто .swapcase():\n")
print(sentense.swapcase())
print("----------------------------------------------------------------------------------")
print("Подстановка тремя способами .format(), %, f:\n")
first_name = "Igor"
last_name = "Makarevich"
print("Hello, {} {}!".format(first_name, last_name))
print("Hello, %s %s!" % (first_name, last_name))
print(f"Hello, {first_name} {last_name}!")
print("----------------------------------------------------------------------------------")

# 7.Развернуть предложение. Я Денис -> Денис Я.
list_with_split_words = sentense_without_punctuation.split(" ")
list_with_split_words.reverse()
print("Шаг.7 - Развернутое предложение: ", " ".join(list_with_split_words))

# 8.Вывести в консоль исходную строку
print("Шаг.8 - Исходное предложение: " + sentense)
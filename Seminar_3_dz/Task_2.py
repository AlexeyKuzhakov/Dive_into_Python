# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter
import codecs

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

with codecs.open('text_task_2.txt', 'r', 'utf-8') as file:
    text = file.read()

print(top_10_words(text))
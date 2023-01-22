"""
Посчитайте кол-во слов в тексте.
Слова отсортируйте в лексикографическом порядке (как в словаре).
Словом считайте всё что отделено пробелом.
Также не забудьте убрать знаки пунктуации (после знака пунктуации обязательно идет пробельный символ - пробел, либо перенос строки).

Слова должны быть записаны символами в нижнем регистре.

Считайте знаками препинания следующие символы: .?!,-:;
"""

"""
Shall I compare thee to a summer’s day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer’s lease hath all too short a date:
Sometime too hot the eye of heaven shines,
And often is his gold complexion dimmed;
And every fair from fair sometime declines,
By chance, or nature’s changing course, untrimmed:
But thy eternal summer shall not fade,
Nor lose possession of that fair thou ow’st;
Nor shall Death brag thou wander’st in his shade
When in eternal lines to time thou grow’st:
So long as men can breathe or eyes can see,
So long lives this, and this gives life to thee.
"""
import sys

text = sys.stdin.read()
arr_lines = text.split('\n')
dict_words = dict()
i = 1
tmp = []
bad_symbols_arr = '? : ; , . ! -'.split()
for l in arr_lines:
    tmp = l.split(' ')
    for el in tmp:
        for ol in bad_symbols_arr:
            if ol in el:
                el = el[0:len(el)-1]
            else:
                pass
            el = el.lower()
        if el not in dict_words:
            if el != '':
                dict_words[el] = i
            else:
                pass
        else:
            dict_words[el] += 1
sorted_dict_words = dict(sorted(dict_words.items()))
for key in sorted_dict_words:
    print(f"{key}:", sorted_dict_words[key])
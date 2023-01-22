# генераторы списков если по-русски

# import sys

# text = sys.stdin.read()
# arr_lines = text.split('\n')
# dict_words = dict()
# i = 1
# tmp = []
# bad_symbols_arr = '? : ; , . ! -'.split()
# for l in arr_lines:
#     tmp = l.split(' ')
#     for el in tmp:
#         for ol in bad_symbols_arr:
#             if ol in el:
#                 el = el[0:len(el)-1]
#             el = el.lower()
#         if el not in dict_words:
#             if el != '':
#                 dict_words[el] = i
#         else:
#             dict_words[el] += 1
# sorted_dict_words = dict(sorted(dict_words.items()))
# for key in sorted_dict_words:
#     print(f"{key}:", sorted_dict_words[key])

# попытка переписать задачу из stepik3
# текст из задачи
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
# i = 1
# tmp = []
bad_symbols_arr = '? : ; , . ! -'.split()


# nums = [i*i for i in [j for j in range(1, 6)]]

a = []
b = []
c = []
d = [[[a.append(el[0:len(el)].lower()) if ol not in el else a.append(el.lower()) for ol in bad_symbols_arr] for el in l.split()] for l in arr_lines]
# e = [for i in a if]
# arr = [i for i in b]


# [el[0:len(el)-1] for ol in bad_symbols_arr if ol in el]

print(a)

# a = {i: j for i, j in zip(a, a)}


# dict_w = [dict(key, value) for key, value in zip(a, a)]
# print(a)
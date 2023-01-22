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
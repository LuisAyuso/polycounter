es_es = ['qwertyuiop', 'asdfghjklñ', 'zxcvbnm,.-']


def get_char_k(keyboard, i, j):
    return keyboard[i][j]


def get_char(i, j):
    return get_char_k(es_es, i, j)

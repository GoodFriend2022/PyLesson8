# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15

# 1. Где операторы?
# 2. Где числовые значения?

# Уровень 1:

# - 1 действие
# - 2 аргумента

# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4

# Уровень 3:
# - Действия имеют приоритет

# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2

sum = lambda x, y: x + y
mult = lambda x, y: x * y
subt = lambda x, y: x - y
div = lambda x, y: x / y

def split_string(exp_string):
    exp = ['+', '-', '/', '*', '(', ')']
    for i in exp:
        if i in exp_string:
            exp_string = exp_string.replace(i, f' {i} ')
    symbol = exp_string.split()
    for i in range(len(symbol)):
        if not symbol[i] in exp:
            symbol[i] = int(symbol[i])
    return symbol

def calc(exp_list):
    i = 1
    while i < len(exp_list) - 1:
        if exp_list[i] == '*':
            exp_list[i] = mult(exp_list[i-1], exp_list[i+1])
            exp_list.pop(i+1)
            exp_list.pop(i-1)
        elif exp_list[i] == '/':
            exp_list[i] = div(exp_list[i-1], exp_list[i+1])
            exp_list.pop(i+1)
            exp_list.pop(i-1)
        else: i += 1
    i = 1
    while i < len(exp_list) - 1:
        if exp_list[i] == '+':
            exp_list[i] = sum(exp_list[i-1], exp_list[i+1])
            exp_list.pop(i+1)
            exp_list.pop(i-1)
        elif exp_list[i] == '-':
            exp_list[i] = subt(exp_list[i-1], exp_list[i+1])
            exp_list.pop(i+1)
            exp_list.pop(i-1)
        else: i += 1
    return exp_list[0]
        
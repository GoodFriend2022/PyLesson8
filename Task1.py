import function as f

exp = input('Введите выражение, которые хотите вычислить \n>>> ')
print(exp)

exp_split = f.split_string(exp)
print(exp_split)
exam = f.calc(exp_split)
print(exam)

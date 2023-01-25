import function as f
import os

os.system('cls')

exp = '2+(5+2*4-(5+5)/2*(1+1))-1'#input('Введите выражение, которые хотите вычислить \n>>> ')
print(exp)

exp_split = f.split_string(exp)
print(exp_split)
exam = f.priority_calc(exp_split)
print(f'Выражение после сокращения скобок будет выглядеть следующим образом: \n{exam}')
result = f.calc(exam)
print(f'В результате вычислений получено = {result}')


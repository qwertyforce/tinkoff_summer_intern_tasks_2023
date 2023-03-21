"""
Набор чисел ﻿x_1, x_2, \dots, x_kx 
1
​
 ,x 
2
​
 ,…,x 
k
​
 ﻿ назовем "скучным", если получается удалить из него один элемент так, чтобы каждое число в данном наборе встречалось одинаковое количество раз. Удаление — обязательная операция.

Дан массив ﻿a_1, a_2, \dots, a_na 
1
​
 ,a 
2
​
 ,…,a 
n
​
 ﻿ длины ﻿nn﻿. Найдите максимальное число ﻿ll﻿ ﻿(2 \leq l \leq n)(2≤l≤n)﻿, что префикс длины ﻿ll﻿ это массива, т.е. его первые ﻿ll﻿ элементов, является скучным набором чисел.

Выведите одно число — максимальное ﻿ll﻿, что префикс длины ﻿ll﻿ массива ﻿aa﻿ является скучным.

13
1 2 3 1 2 2 3 3 3 1 4 4 5 -> 10

10
1 2 4 2 3 1 3 9 15 23 -> 7 

5
1 2 3 4 5 -> 5
"""

from collections import defaultdict
input()
arr = list(map(int, input().split(" ")))
counter = defaultdict(int)
freq_counter = defaultdict(int)
max_freq = 0
ans = 0
for i, num in enumerate(arr):
    counter[num]+=1
    freq_counter[counter[num]-1] -= 1
    freq_counter[counter[num]] += 1
    max_freq = max(max_freq,counter[num])
    if max_freq*freq_counter[max_freq] == i or (max_freq-1)*(freq_counter[max_freq-1]+1) == i or max_freq == 1:
        res = i + 1
print(res)
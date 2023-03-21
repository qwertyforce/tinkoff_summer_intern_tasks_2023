"""
Дана строка ﻿ss﻿, состоящая из символов ﻿aa﻿, ﻿bb﻿, ﻿cc﻿ и ﻿dd﻿.
Подстрокой строки ﻿ss﻿ называется строка, которую можно получить, взяв из ﻿ss﻿ какие-то подряд идущие символы. Например, строки ﻿bcdbcd﻿, ﻿abcdcdababcdcdab﻿, ﻿cdcdabcdcdab﻿ являются подстроками строки ﻿abcdcdababcdcdab﻿, а ﻿cccc﻿ и ﻿cdcdcdcdcdcd﻿ — нет.
Назовем строку хорошей, если каждый из символов ﻿aa﻿, ﻿bb﻿, ﻿cc﻿, ﻿dd﻿ встречается в ней хотя бы один раз.
Найдите длину самой короткой хорошей подстроки строки ﻿ss﻿ или определите, что у ﻿ss﻿ нет хороших подстрок.

Выведите длину самой короткой хорошей подстроки строки ﻿ss﻿. Если хороших подстрок нет, выведите ﻿-1−1﻿.

12
aabbccddbadd -> 5

16
aaaabbbbccccdddd -> 10

7
dbbccca -> 7

7
abcabac -> -1
"""

from collections import defaultdict
input()
s = input()
m = defaultdict(int)
l=0
_m = len(s)+1
for r in range(len(s)):
    m[s[r]]+=1 
    if m["a"]> 0 and m["b"]> 0 and m["c"]> 0 and m["d"]> 0:
        _m=min(_m,r-l+1)
        while m["a"]> 0 and m["b"]> 0 and m["c"]> 0 and m["d"]> 0:
            _m=min(_m,r-l+1)
            m[s[l]]-=1
            l+=1
            
if _m == len(s)+1:
    print(-1)
else:
    print(_m)
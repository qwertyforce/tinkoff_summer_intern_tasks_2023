'''
Четыре человека выстроились в очередь друг за другом. Определите, правда ли, что они стоят по росту (неважно, в порядке неубывания или порядке невозрастания).
Выведите YES, если люди выстроены в порядке неубывания или невозрастания их роста, и NO в противном случае.

1 2 3 4 -> YES
7 6 5 5 -> YES
4 4 4 4 -> YES
5 2 3 1 -> NO
'''

h1,h2,h3,h4 = list(map(int, input().split(" ")))
if h1<=h2<=h3<=h4:
    print("YES")
elif h1>=h2>=h3>=h4:
    print("YES")
else:
    print("NO")
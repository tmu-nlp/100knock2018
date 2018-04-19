import knock05

s1 = 'paraparaparadise'
s2 = 'paragraph'
X = set(knock05.n_gram(2, s1, knock05.CHAR))
Y = set(knock05.n_gram(2, s2, knock05.CHAR))

print(f'{"X":<15}: {X}')
print(f'{"Y":<15}: {Y}')
print(f'{"Union":<15}: {X | Y}')
print(f'{"Intersection":<15}: {X & Y}')
print(f'{"Difference(X-Y)":<15}: {X - Y}')
print(f'{"Difference(Y-X)":<15}: {Y - X}')
print(f"Is 'se' belong to X? -> {'se' in X}")
print(f"Is 'se' belong to Y? -> {'se' in Y}")

# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi - gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi - gramがXおよびYに含まれるかどうかを調べよ．

# 実行結果
# X              : {'is', 'pa', 'ra', 'ad', 'ar', 'se', 'ap', 'di'}
# Y              : {'gr', 'ag', 'ph', 'pa', 'ra', 'ar', 'ap'}
# Union          : {'gr', 'ag', 'ph', 'is', 'pa', 'ra', 'ad', 'ar', 'se', 'ap', 'di'}
# Intersection   : {'ra', 'ar', 'ap', 'pa'}
# Difference(X-Y): {'ad', 'is', 'di', 'se'}
# Difference(Y-X): {'ag', 'gr', 'ph'}
# Is 'se' belong to X? -> True
# Is 'se' belong to Y? -> False

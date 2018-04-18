fmt = "{x}時の{y}は{z}"
data = dict(x=12, y="気温", z=22.4)
print(fmt.format(**data))

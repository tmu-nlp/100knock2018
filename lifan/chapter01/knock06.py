from knock05 import get_string_bigram

list_x = get_string_bigram("paraparaparadise")
list_y = get_string_bigram("paragraph")

print("X:", set(list_x))
print("Y:", set(list_y))
print("和集合:", set(list_x) | set(list_y))
print("積集合:", set(list_x) & set(list_y))
print("差集合:", set(list_x) - set(list_y))
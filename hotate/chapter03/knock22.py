from knock20 import extraction
import re


def category(s):
    pattern = r'Category:(.*?)(?:\||\])'
    l = re.findall(pattern, s)
    return l


if __name__ == '__main__':
    s = extraction('イギリス')
    print(category(s))

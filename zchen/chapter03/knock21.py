from knock20 import filter_english

def line_with_category():
    for line in filter_english():
        if 'Category' in line:
            yield line

if __name__ == "__main__":
    print("'Category in 'イギリス':")
    for i in line_with_category():
        print(i)

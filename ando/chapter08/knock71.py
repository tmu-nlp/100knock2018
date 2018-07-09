def stop_check(word,stoplist):
    if word in stoplist:
        return True
    return False

if __name__ == "__main__":
    list_ = []
    for line in open("stop.txt","r"):
        list_.append(line.strip())
    print(stop_check("a",list_))
    print(stop_check("book",list_))
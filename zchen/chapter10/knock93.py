from knock91 import load_analogy

if __name__ == '__main__':
    lt5 = load_analogy('knock92.txt', 5)['family+1']
    n = len(lt5)
    c = sum(1 for t5 in lt5 if t5[3] == t5[4])
    print('accuracy:', c/n)

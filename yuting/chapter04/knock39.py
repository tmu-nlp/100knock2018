#Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．



import knock30
import knock36
import matplotlib.pyplot as plt


def plot_words_hist_log(counter, file):

    plt.figure()
    plt.xscale('log')
    plt.yscale('log')
    plt.plot(sorted(list(counter.values()), reverse=True), range(1, len(list(counter))+1))
    plt.savefig(file)


if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_words_hist_log.png'
    f = open(inputfile, 'r')
    words = []
    counts = []
    sentences = knock30.mecab_reader(f)
    counter = knock36.count_word(sentences)
    plot_words_hist_log(counter, outputfile)
    f.close()
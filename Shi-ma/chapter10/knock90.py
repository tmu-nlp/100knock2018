from gensim.models import word2vec
import os.path


if __name__ == '__main__':
    path_model = 'result/knock90.bin'

    if not os.path.exists(path_model):
        data = word2vec.LineSentence('../chapter09/result/knock81_result.txt')
        model = word2vec.Word2Vec(data, min_count=1, window=3, size=100)
        model.save(path_model)
    else:
        model = word2vec.Word2Vec.load(path_model)

    with open('result/knock90.txt', 'w') as data_out:
        print('<knock86_result>', file=data_out)
        print(model['United_States'], file=data_out)

        print('\n<knock87_result>', file=data_out)
        print(model.similarity('United_States', 'U.S'), file=data_out)

        print('\n<knock88_result>', file=data_out)
        simi_England = model.most_similar('England', topn=10)
        print('\n'.join(map(lambda x: '{}'.format(x), simi_England)), file=data_out)

        print('\n<knock89_result>', file=data_out)
        simi_Answer = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
        print('\n'.join(map(lambda x: '{}'.format(x), simi_Answer)), file=data_out)

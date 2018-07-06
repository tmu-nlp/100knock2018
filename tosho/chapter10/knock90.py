from gensim.models import word2vec
from sys import argv

def main():
    data_path = argv[1]
    model_path = argv[2]

    sentences = word2vec.LineSentence(data_path)
    model = word2vec.Word2Vec(sentences)

    model.save(model_path)
    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')


import sys, os
sys.path.append(os.pardir)
from chapter06.knock53 import load_nlp_sentences
from common.parsers import load_corenlp_dependencies
from collections import defaultdict
from itertools import islice

def load_nlp_deps(file_name='./nlp.txt.xml', nth=None):
    if nth is None:
        return load_corenlp_dependencies(file_name)
    else:
        return next(islice(load_corenlp_dependencies(file_name), nth-1, nth))

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from matplotlib.image import imread
    from common.drawers import draw_corenlp_dependencies
    
    s_id, deps = load_nlp_deps(nth=1)

    draw_corenlp_dependencies(deps, 'knock57.png')

    img = imread('knock57.png')
    plt.imshow(img)
    plt.show()

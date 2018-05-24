
if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks
    from common.drawers import draw_dependency_graph

    import matplotlib.pyplot as plt
    from matplotlib.image import imread

    chunks = get_neko_chunks(8)

    draw_dependency_graph(chunks, 'knock44.png')

    img = imread('knock44.png')
    plt.imshow(img)
    plt.show()